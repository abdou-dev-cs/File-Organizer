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

| Category     | Extensions              |
| ------------ | ----------------------- |
| Images       | .jpg, .jpeg, .png, .gif |
| Documents    | .pdf, .docx, .txt       |
| Music        | .mp3                    |
| Videos       | .mp4, .avi, .mkv        |
| Archives     | .zip, .rar              |
| Python Files | .py                     |
| Spreadsheets | .xlsx, .csv             |

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
