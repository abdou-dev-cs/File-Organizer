# File Organizer

A Python automation tool that automatically organizes files into categorized folders based on their file extensions. This project helps users keep their directories clean and structured by sorting files into predefined categories such as Images, Documents, Music, Videos, Archives, and more.

## Features

* Automatically organizes files by extension
* Creates category folders when they do not exist
* Supports multiple file types
* Works with any user-specified directory
* Simple and lightweight command-line interface
* Fast and efficient file management

## Supported Categories

| Category            | Extensions |
| ------------------- | ---------- |
| Images              | .jpg, .jpeg, .png, .gif, .bmp, .webp, .svg, .tiff, .tif, .ico, .heic, .heif, .raw, .psd, .ai, .eps, .avif |
| PDF                 | .pdf |
| Word Documents      | .doc, .docx, .odt, .rtf |
| Text Files          | .txt, .md, .tex, .log |
| PowerPoint          | .ppt, .pptx, .pptm, .odp, .key |
| Spreadsheets        | .xls, .xlsx, .xlsm, .xlsb, .csv, .tsv, .ods |
| Music               | .mp3, .wav, .aac, .flac, .ogg, .wma, .m4a, .opus, .mid, .midi, .aiff |
| Videos              | .mp4, .avi, .mkv, .mov, .wmv, .webm, .m4v, .flv, .3gp, .mpeg, .mpg, .ts, .mts |
| Archives            | .zip, .rar, .7z, .tar, .gz, .bz2, .xz, .tgz, .iso, .cab, .zst |
| Python Files        | .py, .pyc, .ipynb |
| Flutter             | .dart |
| Flutter / Dart      | .dart |
| Programming Files   | .java, .class, .kt, .js, .jsx, .ts, .tsx, .php, .html, .css, .scss, .c, .cpp, .h, .hpp, .cs, .go, .rs, .rb, .swift, .vue, .sh, .bat, .ps1 |
| Databases           | .db, .sql, .sqlite, .sqlite3, .db3, .mdb, .accdb, .fdb, .gdb, .nsf, .pdb, .sdf, .sqlite2, .sqlite4, .dbf, .parquet, .bson, .rdb |
| Executables         | .exe, .msi, .dll, .sys, .app, .deb, .rpm, .apk, .aab |
| Fonts               | .ttf, .otf, .woff, .woff2 |
| 3D Models           | .obj, .stl, .fbx, .blend, .gltf, .glb |
| Configuration Files | .ini, .cfg, .conf, .toml, .env, .json, .yaml, .yml, .xml |
| E-books             | .epub, .mobi |
| Virtual Machines    | .vmdk, .vdi, .vhd, .vhdx, .ova |

**Note:** Files with unsupported or unrecognized extensions are automatically categorized as `Others`.

## Project Structure

```text
file-organizer/
│
├── organizer.py
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/abdou-dev-cs/file-organizer.git
cd file-organizer
```

## Usage

Run the application:

```bash
python organizer.py
```

Enter the target folder path when prompted.

Example:

```text
Enter folder path: D:\Downloads
```

> [!WARNING]
> **Important: Avoid Using the Root of the C: Drive**
>
> When running this script, **DO NOT provide `C:\` (the root of your system drive) as the target directory.**
>
> The script automatically organizes files by moving them into categorized folders. Running it on the root of your system drive may move important system files, application files, or other critical data, potentially causing system errors or unexpected behavior.
>
> **Recommended:** Always use a specific folder or directory containing files you want to organize (e.g., `C:\Users\YourName\Downloads` or `D:\MyFiles`).
>
> **Safety First:** Use this tool only on directories you have explicitly selected and whose contents you are comfortable reorganizing.

The program will automatically create the necessary folders and move files into their corresponding categories.

## Technologies Used

* Python 3
* os
* pathlib
* shutil

## Learning Objectives

This project was created to practice:

* File and directory manipulation
* Working with Python standard libraries
* Automation scripting
* Project structure and organization
* Error handling
* Git and GitHub workflow

## Future Improvements

* Graphical User Interface (GUI)
* Custom user-defined categories
* Duplicate file detection
* Logging system
* Automatic scheduled organization
* AI-powered file categorization

## Author

**Abderrahmane Abdou**

Software Engineering Student | Flutter Developer | Python & AI Enthusiast
