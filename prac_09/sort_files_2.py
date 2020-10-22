"""
CP1404 File sorting program Part 2
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

    # Loop through available file extensions and ask which folder to put in and add to dictionary
    directory_for_extensions = {}
    for extension in file_extensions:
        # Ask for new directory name
        new_directory = input("What category would you like to sort {} files into? ".format(extension))

        # Make dictionary to associate extension to directory
        if extension not in directory_for_extensions:
            directory_for_extensions[extension] = new_directory

        # Try to make new directory
        try:
            os.mkdir(new_directory)
        except FileExistsError:
            pass

    # Add files to correct directory
    for extension in directory_for_extensions:
        file_destination = directory_for_extensions[extension]
        for filename in os.listdir('.'):
            if extension in filename:
                shutil.move(filename, file_destination)


main()
