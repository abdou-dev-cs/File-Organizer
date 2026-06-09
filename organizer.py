import shutil
from pathlib import Path
import os


def get_category(extension):
    if extension in [".jpg", ".png", ".jpeg"]:
        return "Images"

    elif extension in [".pdf", ".docx", ".txt"]:
        return "Documents"

    elif extension == ".mp3":
        return "Music"

    elif extension in [".mp4", ".avi", ".mkv"]:
        return "Videos"

    elif extension in [".zip", ".rar"]:
        return "Archives"

    elif extension == ".py":
        return "Python"

    elif extension in [".xlsx", ".csv"]:
        return "Spreadsheets"

    return "Others"


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def move_file(file_path, destination):
    shutil.move(file_path, destination)


def organize_folder(folder_path):
    files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    for file in files:
        # We get all extensions of all files
        extension = Path(file).suffix.lower()
        # We get the correct category
        category = get_category(extension)
        # We add the category to the path to get the destination path (1)
        category_folder = os.path.join(folder_path, category)
        # We creat the folder in the specified path
        create_folder(category_folder)
        # We add the the file to the path to get the file we want to move (2)
        source = os.path.join(folder_path, file)
        # Mix (1) and (2)
        destination = os.path.join(category_folder, file)
        # Move the file
        move_file(source, destination)


if __name__ == "main":
    folder = input("Enter folder path that you wish to be organized: ")
    organize_folder(folder)
    print("Folder organized successfully!")