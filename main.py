#! /usr/bin/env python3

import os
import shutil

from tkinter import filedialog


def main():
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
            print(destination)


def convert_filename(old_filename, source_folder):
    new_filename = old_filename.replace(" ", "_")
    return shutil.move(
        os.path.join(source_folder, old_filename),
        os.path.join(source_folder, new_filename),
    )


if __name__ == "__main__":
    source_folder = filedialog.askdirectory(mustexist=True)
    home_directory = os.path.expanduser("~")
    main()
