import base64
import hashlib
import json
import os
from pathlib import Path
from shutil import copyfileobj
import subprocess
import time
from urllib.parse import quote, urlsplit
from zipfile import ZipFile

import requests

root = Path(os.environ["RUNNER_TEMP"])
repo = "FORQO/RoadMax-Public"
api = f"https://api.github.com/repos/{repo}"
branch = "distribution/roadmax-2.3.23"
target = "e0dcc786120a8ee9cf1f488da4ce9daaa54bc8fd"
tag = "v2.3.23"
intel = "RoadMax-2.3.23-macOS-x64.dmg"
windows = "RoadMax-Portable-2.3.23.exe"
arm = "RoadMax-2.3.23-macOS-arm64.dmg"
checks = "SHA256SUMS.txt"
auth = {"Authorization": "Bearer " + os.environ["GH_TOKEN"], "Accept": "application/vnd.github+json"}
session = requests.Session()

def require(ok, message):
    if not ok:
        raise SystemExit(message)

def gh(method, path, **options):
    response = session.request(method, api + path, headers=auth, timeout=90, **options)
    require(response.ok, f"GitHub {method} {path} failed with HTTP {response.status_code}")
    return response.json()

manifest = gh("GET", "/contents/docs/RELEASE-MANIFEST.json", params={"ref": target})
assets = {x["name"]: x for x in json.loads(base64.b64decode(manifest["content"]))["assets"]}
require(set(assets) == {intel, windows, arm, checks}, "Unexpected manifest")

def remote_ok(asset):
    expected = assets.get(asset["name"])
    return (expected and asset["state"] == "uploaded" and asset["size"] == expected["bytes"]
            and asset["digest"] == "sha256:" + expected["sha256"])

def local_ok(path, digest):
    with path.open("rb") as source:
        require(hashlib.file_digest(source, "sha256").hexdigest() == digest, "Digest mismatch: " + path.name)

def list_assets(release_id):
    return gh("GET", f"/releases/{release_id}/assets")

drafts = []
for release in gh("GET", "/releases", params={"per_page": 50}):
    if release["draft"] and {windows, arm} <= {a["name"] for a in release["assets"] if remote_ok(a)}:
        drafts.append(release)
require(len(drafts) == 1, "Expected exactly one draft with the approved Windows and Apple Silicon builds")
release_id = drafts[0]["id"]
existing = list_assets(release_id)
require(all(remote_ok(a) for a in existing), "Unexpected assets already attached to draft")
present = {a["name"] for a in existing}

if intel not in present:
    encrypted = root / "envelope.der"
    for _ in range(210):
        r = session.get(api + "/contents/handoff/intel-2.3.23.cms.b64", headers=auth, params={"ref":branch}, timeout=25)
        if r.status_code == 200:
            encrypted.write_bytes(base64.b64decode(base64.b64decode(r.json()["content"]).strip(), validate=True))
            break
        require(r.status_code == 404, "Cannot check release handoff")
        time.sleep(5)
    require(encrypted.exists(), "Release handoff timed out")
    proc = subprocess.run(["openssl", "cms", "-decrypt", "-binary", "-inform", "DER", "-in", str(encrypted),
                           "-recip", "handoff/receiver-2.3.23.pem", "-inkey", str(root/"recipient.key")], capture_output=True)
    require(proc.returncode == 0, "Cannot decrypt release handoff")
    (root/"recipient.key").unlink()
    location = proc.stdout.decode().strip()
    parsed = urlsplit(location)
    require(parsed.scheme == "https" and parsed.hostname and not parsed.username and not parsed.password and
            (parsed.hostname.endswith(".blob.core.windows.net") or parsed.hostname.endswith(".githubusercontent.com")
             or parsed.hostname.endswith(".actions.githubusercontent.com")), "Unexpected artifact host")
    archive = root/"verified-intel.zip"
    try:
        with requests.get(location, stream=True, timeout=(20, 120), allow_redirects=False) as body, archive.open("wb") as out:
            require(body.status_code == 200, f"Artifact download returned HTTP {body.status_code}")
            for chunk in body.iter_content(1024*1024):
                out.write(chunk)
    except requests.RequestException:
        raise SystemExit("Artifact transfer failed") from None
    local_ok(archive, "0690786fc53fba666cd1a76f650d784e3abd170987946f5b36556180b40149b8")
    with ZipFile(archive) as z:
        items = [i for i in z.infolist() if i.filename.split("/")[-1] == intel]
        require(len(items) == 1 and items[0].file_size == assets[intel]["bytes"], "Unexpected ZIP contents")
        with z.open(items[0]) as source, (root/intel).open("wb") as out:
            copyfileobj(source, out)

(root/checks).write_bytes("".join(f"{assets[name]['sha256']}  {name}\n" for name in sorted([windows, arm, intel])).encode())
for name in [intel, checks]:
    if name in present:
        continue
    path = root/name
    local_ok(path, assets[name]["sha256"])
    with path.open("rb") as data:
        r = requests.post(f"https://uploads.github.com/repos/{repo}/releases/{release_id}/assets",
                          params={"name":name}, headers={**auth, "Content-Type": "application/octet-stream"}, data=data, timeout=240)
    require(r.status_code == 201 and remote_ok(r.json()), f"Upload verification failed for {name}, HTTP {r.status_code}")
    print("Verified upload", name, flush=True)

finished = list_assets(release_id)
require(len(finished) == 4 and {a["name"] for a in finished if remote_ok(a)} == set(assets), "Release verification failed")
body = """В RoadMax 2.3.23 ускорена отрисовка точечной сетки при перемещении и масштабировании доски. Исправление проверено на доске со 180 стикерами и 24 штрихами.

| Система | Файл для скачивания |
| --- | --- |
| Windows 10 и 11, x64 | `RoadMax-Portable-2.3.23.exe` |
| macOS 13 и новее, Apple Silicon (серия M) | `RoadMax-2.3.23-macOS-arm64.dmg` |
| macOS 13 и новее, Intel | `RoadMax-2.3.23-macOS-x64.dmg` |

Перед обновлением сохраните доску и закройте предыдущую версию. Файл `SHA256SUMS.txt` содержит контрольные суммы всех трёх сборок.

[Официальный сайт RoadMax](https://roadmax.dskforge.com/) · [Инструкция по началу работы](https://github.com/FORQO/RoadMax-Public/blob/main/docs/QUICK-START-RU.md)"""
live = gh("PATCH", f"/releases/{release_id}", json={"tag_name":tag, "target_commitish":target,
          "name":"RoadMax 2.3.23 — плавное масштабирование с точечной сеткой", "body":body, "draft":False, "prerelease":False, "make_latest":"true"})
require(not live["draft"] and live["tag_name"] == tag, "Published release metadata mismatch")
print(live["html_url"])
