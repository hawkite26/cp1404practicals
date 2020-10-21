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

    # Extensions list
    file_extensions = []

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        # Find file extension type
        file_extension_index = filename.find('.')
        file_extension = filename[file_extension_index + 1:]

        # Add file extension to list if not found in list
        if file_extension not in file_extensions:
            file_extensions.append(file_extension)

    print(file_extensions)


main()
