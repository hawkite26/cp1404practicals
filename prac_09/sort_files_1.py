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

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue




main()
