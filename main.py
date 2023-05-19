#! /usr/bin/env python3

import os
import sys
import shutil
import logging

from tkinter import filedialog

home_directory = os.path.expanduser("~")
logging.basicConfig(
    filename=os.path.join(home_directory, "File-Transfer-Log.txt"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def file_transfer(source_folder, home_directory):
    """Transfer files from source_folder to appropriate directories.

    Args:
        source_folder (str): folder to manage selected by user.
        home_directory (str): home directory file path.
    """
    for file in os.listdir(source_folder):
        # Rename file if it contains space.
        if " " in file:
            # print(str(file) + ' contains space!')
            file = convert_filename(file, source_folder)

        # Detect file type and move to appropriate directory.
        if file.endswith((".mkv", ".mp4")):
            target = "Videos"
            transfer(target, source_folder, file)
        if file.endswith((".mp3", ".aac", ".ogg", ".flac", ".wav")):
            target = "Music"
            transfer(target, source_folder, file)
        if file.endswith((".svg", ".png", ".jpg", ".jpeg")):
            target = "Pictures"
            transfer(target, source_folder, file)
        if file.endswith((".pdf", ".docx", ".xlsx", ".csv", ".ppt")):
            target = "Documents"
            transfer(target, source_folder, file)


def transfer(target, source_folder, file):
    destination = shutil.move(
        os.path.join(source_folder, file),
        os.path.join(home_directory, target),
    )
    destination = os.path.dirname(destination)
    logging.info("Moved " + file + " to " + destination)
    print("Moved \033[35m" + file +
          "\033[39m to \033[33m" + destination + "\033[39m")


def convert_filename(old_filename, source_folder):
    """Convert invalid filenames to valid filenames.

    Args:
        old_filename (str): invalid filename.
        source_folder (str): source folder to get filenames from.

    Returns:
        str: absolute filepath to the new valid filename.
    """
    new_filename = old_filename.replace(" ", "_")
    return shutil.move(
        os.path.join(source_folder, old_filename),
        os.path.join(source_folder, new_filename),
    )


def main():
    source_folder = filedialog.askdirectory(mustexist=True)
    if source_folder == () or source_folder == '':
        print("\n\nYou gotta give me a source. ¯\_(ツ)_/¯\n\n")
        sys.exit()
    file_transfer(source_folder, home_directory)


if __name__ == "__main__":
    main()
