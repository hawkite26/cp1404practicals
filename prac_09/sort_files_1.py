"""
CP1404 File sorting program
Kye Bryce
"""

import os
import shutil


def main():
    """File sorter for FilesToSort"""

    # Enter directory
    os.chdir('FilesToSort')

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        # Find file extension type
        file_extension_index = filename.find('.')
        file_extension = filename[file_extension_index + 1:]

        # Make new directories with file extension type
        try:
            os.mkdir(file_extension)
        except FileExistsError:
            pass

        # Add files to corresponding folders
        shutil.move(filename, file_extension)


main()
