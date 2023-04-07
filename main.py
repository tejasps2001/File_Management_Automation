#! /usr/bin/env python3

import os
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
            destination = shutil.move(
                os.path.join(source_folder, file),
                os.path.join(home_directory, "Videos"),
            )
            destination = os.path.dirname(destination)
            logging.info("Moved " + file + " to " + destination)
            print(
                "Moved \033[35m"
                + file
                + "\033[39m to \033[33m"
                + destination
                + "\033[39m"
            )


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
    file_transfer(source_folder, home_directory)


if __name__ == "__main__":
    main()
