# RoadMax

[Русская версия](README.md)

RoadMax is an offline whiteboard for Windows and macOS. Pin a source PDF next to your notes, mark a passage, and draw an arrow to the decision it supports. Boards and attachments stay on your computer. This public repository hosts desktop downloads, examples and user documentation.

| Download RoadMax 2.4.0 | How to open it |
| --- | --- |
| [Windows 10/11 · x64 Portable](https://github.com/FORQO/RoadMax-Public/releases/download/v2.4.0/RoadMax-Portable-2.4.0.exe) | Run the EXE. |
| [macOS 13+ · Apple Silicon](https://github.com/FORQO/RoadMax-Public/releases/download/v2.4.0/RoadMax-2.4.0-macOS-arm64.dmg) | Open the DMG and drag RoadMax into Applications. |
| [macOS 13+ · Intel](https://github.com/FORQO/RoadMax-Public/releases/download/v2.4.0/RoadMax-2.4.0-macOS-x64.dmg) | Open the DMG and drag RoadMax into Applications. |

On a Mac, **About This Mac** shows whether you have an Apple chip or an Intel processor. The Windows executable is unsigned and the Mac builds are distributed without Apple notarization. To update, back up your work and quit the earlier version first. [Latest release and SHA-256 checksums](https://github.com/FORQO/RoadMax-Public/releases/latest)

[![A RoadMax board with project notes, connections and documents](assets/screenshots/2.4.0/en/board-light.webp)](assets/screenshots/2.4.0/en/board-light.webp)

*The board shows “North Quay field survey”, a demonstration project about access along a waterfront, in RoadMax 2.4.0.*

To choose a language, open **Language** (or **Язык**), select **English** or **Русский**, and confirm the restart. **Use system language** follows your system’s preferred languages. RoadMax uses English when none of them is supported.

## Try a board

1. [Download “One Street, Three Photographs” (ZIP)](https://github.com/FORQO/RoadMax-Public/raw/refs/heads/main/examples/one-street-en.zip) and extract the archive. It contains one board with four editable sticky notes for planning a small exhibition.
2. In RoadMax, choose **File → Open RoadMax project…** and select `one-street-en.roadmax` from the archive.
3. Add a photo or PDF next to **Source material**. Write down a detail you noticed and draw an arrow from the note to its source.

## What’s new in 2.4.0

- In a PDF, select a passage and choose **Quote to board**. The card links back to its source page. **Beside board** keeps the PDF and canvas open together.
- In the library, open a project and search for words in its documents. A PDF match points to a page and a DOCX match points to a paragraph. Turn on **Recognize scans (OCR)** to search printed English and Russian text in scanned PDF pages offline. This setting starts off for new profiles.
- **File → Show current project folder** opens the folder containing `Project.roadmax`, the boards and attachments. RoadMax writes current working files to `Files/<board name>`. If you edit a file in another app, RoadMax preserves that copy. Import it explicitly to use those external edits on the board. To continue on another computer, close RoadMax and copy the whole project folder.
- Export a board, selection or named area as a standalone HTML file. Original attachments are included only when you select them.

## Screenshots

| View | Light theme | Dark theme |
| --- | --- | --- |
| Board | [Light](assets/screenshots/2.4.0/en/board-light.webp) | [Dark](assets/screenshots/2.4.0/en/board-dark.webp) |
| Project library | [Light](assets/screenshots/2.4.0/en/library-light.webp) | [Dark](assets/screenshots/2.4.0/en/library-dark.webp) |
| PDF | [Light](assets/screenshots/2.4.0/en/pdf-light.webp) | [Dark](assets/screenshots/2.4.0/en/pdf-dark.webp) |
| Image editor | [Light](assets/screenshots/2.4.0/en/image-light.webp) | [Dark](assets/screenshots/2.4.0/en/image-dark.webp) |
| Spreadsheet | [Light](assets/screenshots/2.4.0/en/sheet-light.webp) | [Dark](assets/screenshots/2.4.0/en/sheet-dark.webp) |
| DOCX | [Light](assets/screenshots/2.4.0/en/docx-light.webp) | [Dark](assets/screenshots/2.4.0/en/docx-dark.webp) |
| PDF quote and source | [Light](assets/screenshots/2.4.0/en/quote-light.webp) | [Dark](assets/screenshots/2.4.0/en/quote-dark.webp) |
| Project folder commands | [Light](assets/screenshots/2.4.0/en/folders-light.webp) | [Dark](assets/screenshots/2.4.0/en/folders-dark.webp) |

[Compare line and dot grids in both themes](assets/screenshots/2.4.0/en/grid.webp). Lines are on the left and dots on the right.

## Follow a quote back to its source

[Try the interactive board on the website](https://roadmax.dskforge.com/#interactive-board) or [download the example project and PDF](https://github.com/FORQO/RoadMax-Public/raw/c14cd882f7a3f6a7f166b4e3315a1a7a7ea2bd24/examples/north-quay-quote-2.4.0.zip). Extract the whole ZIP, keep the `Attachments` folder next to `North Quay field notes.roadmax`, and open the project in RoadMax 2.4.0. The quote about a sign points to page 2 of the field notes.

To share your own board, choose **File → Export interactive HTML…**. Choose the whole board, selected objects or a named area. Tick an attachment only if you want to share its original file. The HTML opens offline in a browser and supports panning, zooming and following a quote to its source card.

## Working with your own files

You can annotate PDFs and images and edit supported XLSX, CSV, TSV and DOCX files. Complex Office documents can open read-only. Project search can recognize printed Russian and English text on scanned PDF pages. Selecting text in the PDF viewer requires a text layer. RoadMax keeps original attachments separately from edited versions.

To move a board to another computer, choose **File → Save project to folder…** and copy the entire exported folder, including its attachments. Open the `.roadmax` file on the other computer.

[Official website](https://roadmax.dskforge.com/) · [File support and limitations · Russian](README.md#форматы-и-ограничения) · [Ask a question or report a problem](https://github.com/FORQO/RoadMax-Public/issues/new/choose)
