import os
import shutil

from tkinter import filedialog
def main():
    for file in os.listdir(source_folder):
        # Rename file if it contains space.
        if ' ' in file:
            # print(str(file) + ' contains space!')
            file = convert_filename(file)

def convert_filename(old_filename):
    return old_filename.replace(' ', '_')

if __name__ == '__main__':
    source_folder = filedialog.askdirectory(mustexist=True)
    home_directory = os.path.expanduser('~')
    main()