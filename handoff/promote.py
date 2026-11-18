import base64
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time
from urllib.parse import urlsplit
from zipfile import ZipFile

import requests

REPO = "FORQO/RoadMax-Public"
API = f"https://api.github.com/repos/{REPO}"
BRANCH = "operations/promote-roadmax-2.3.24"
TAG = "v2.3.24"
BINARIES = {"RoadMax-Portable-2.3.24.exe", "RoadMax-2.3.24-macOS-arm64.dmg", "RoadMax-2.3.24-macOS-x64.dmg"}
TEMP = Path(os.environ["RUNNER_TEMP"])
CHANNEL = os.environ["GITHUB_RUN_ID"] + "-" + os.environ["GITHUB_RUN_ATTEMPT"]
AUTH = {"Authorization": "Bearer " + os.environ["GH_TOKEN"], "Accept": "application/vnd.github+json"}


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def api(method, path, **kwargs):
    response = requests.request(method, API + path, headers=AUTH, timeout=75, **kwargs)
    check(response.ok, f"GitHub returned {response.status_code} for {method} {path}")
    return response.json()


def contents(path, ref):
    entry = api("GET", "/contents/" + path, params={"ref": ref})
    return base64.b64decode(entry["content"])


def receive_links():
    cipher = TEMP / "handoff.der"
    for _ in range(200):
        resp = requests.get(f"{API}/contents/handoff/urls-{CHANNEL}.cms.b64", headers=AUTH,
                            params={"ref": BRANCH}, timeout=30)
        if resp.status_code == 200:
            cipher.write_bytes(base64.b64decode(base64.b64decode(resp.json()["content"]).strip(), validate=True))
            break
        check(resp.status_code == 404, "Cannot read release handoff")
        time.sleep(5)
    check(cipher.is_file(), "Release handoff timed out")
    key = TEMP / "recipient.key"
    proc = subprocess.run(["openssl", "cms", "-decrypt", "-binary", "-inform", "DER",
                           "-in", str(cipher), "-recip", f"handoff/receiver-{CHANNEL}.pem", "-inkey", str(key)],
                          capture_output=True)
    key.unlink()
    check(proc.returncode == 0, "Cannot open release handoff")
    links = json.loads(proc.stdout)
    check(set(links) == BINARIES, "Unexpected file names in handoff")
    return links


def sha256(path):
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def retrieve(name, location, archive_hash, asset):
    parsed = urlsplit(location)
    check(parsed.scheme == "https" and not parsed.username and not parsed.password and parsed.hostname and
          (parsed.hostname.endswith(".blob.core.windows.net") or parsed.hostname.endswith(".githubusercontent.com")),
          "Unexpected GitHub artifact storage location")
    archive = TEMP / (name + ".zip")
    try:
        with requests.get(location, stream=True, allow_redirects=False, timeout=(20, 90)) as response:
            check(response.status_code == 200, f"HTTP {response.status_code} downloading {name}")
            with archive.open("wb") as out:
                for chunk in response.iter_content(1024 * 1024):
                    out.write(chunk)
    except requests.RequestException:
        raise RuntimeError(f"Artifact transfer failed for {name}") from None
    check(sha256(archive) == archive_hash, "Archive checksum mismatch for " + name)
    path = TEMP / name
    with ZipFile(archive) as zipped:
        candidates = [i for i in zipped.infolist() if i.filename.rsplit("/", 1)[-1] == name]
        check(len(candidates) == 1 and candidates[0].file_size == asset["bytes"], "Unexpected ZIP for " + name)
        with zipped.open(candidates[0]) as source, path.open("wb") as out:
            shutil.copyfileobj(source, out)
    check(sha256(path) == asset["sha256"], "Installer checksum mismatch for " + name)
    print("Validated", name, flush=True)


def validate_remote(release_id, manifest):
    files = api("GET", f"/releases/{release_id}/assets")
    found = set()
    for file in files:
        name = file["name"]
        check(name in manifest and name not in found, "Unexpected release file")
        spec = manifest[name]
        check(file["state"] == "uploaded" and file["size"] == spec["bytes"] and
              file.get("digest") == "sha256:" + spec["sha256"], "Existing file differs: " + name)
        found.add(name)
    return found


def main():
    config = json.loads(Path("handoff/verified.json").read_text())
    target = config["target"]
    document = json.loads(contents("docs/RELEASE-MANIFEST.json", target))
    manifest = {s["name"]: s for s in document["assets"]}
    check(document["version"] == TAG[1:] and set(manifest) == BINARIES | {"SHA256SUMS.txt"} and
          set(config["archives"]) == BINARIES, "Unexpected release manifest")
    links = receive_links()
    with ThreadPoolExecutor(max_workers=len(BINARIES)) as pool:
        transfers = [pool.submit(retrieve, name, links[name], config["archives"][name], manifest[name])
                     for name in sorted(BINARIES)]
        for transfer in transfers:
            transfer.result()
    sums = TEMP / "SHA256SUMS.txt"
    sums.write_bytes("".join(f"{manifest[n]['sha256']}  {n}\n" for n in sorted(BINARIES)).encode("ascii"))
    check(sha256(sums) == manifest[sums.name]["sha256"] and sums.stat().st_size == manifest[sums.name]["bytes"],
          "Checksum file differs from manifest")
    releases = [r for r in api("GET", "/releases", params={"per_page": 100}) if r["tag_name"] == TAG]
    check(len(releases) <= 1, "Ambiguous release tag")
    info = {"tag_name": TAG, "target_commitish": target, "prerelease": False,
            "name": config["title"], "body": config["body"]}
    release = releases[0] if releases else api("POST", "/releases", json={**info, "draft": True})
    release_id = release["id"]
    present = validate_remote(release_id, manifest)
    if not release["draft"]:
        check(present == set(manifest) and api("GET", "/releases/latest")["tag_name"] == TAG,
              "Existing live release differs")
        return
    for name in sorted(set(manifest) - present):
        with (TEMP / name).open("rb") as data:
            r = requests.post(f"https://uploads.github.com/repos/{REPO}/releases/{release_id}/assets",
                              params={"name": name}, headers={**AUTH, "Content-Type": "application/octet-stream"},
                              data=data, timeout=300)
        check(r.status_code == 201, f"Upload returned HTTP {r.status_code} for {name}")
    check(validate_remote(release_id, manifest) == set(manifest), "Release files incomplete")
    live = api("PATCH", f"/releases/{release_id}", json={**info, "draft": False, "make_latest": "true"})
    check(not live["draft"] and api("GET","/releases/latest")["tag_name"] == TAG, "Release was not published")
    print(live["html_url"])


if __name__ == "__main__":
    main()
