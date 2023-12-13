import os
import shutil
import argparse

def file_folder_creator(directory):
    # List all files in the directory
    files = os.listdir(directory)

    # Iterate over each file
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(directory, file)

        # Check if it is a file (not a subdirectory)
        if os.path.isfile(file_path):
            # Extract the file name without extension
            file_name = os.path.splitext(file)[0]

            # Create a folder with the same name as the file (if it doesn't exist)
            folder_path = os.path.join(directory, file_name)
            os.makedirs(folder_path, exist_ok=True)

            # Move the file to the created folder
            new_file_path = os.path.join(folder_path, file)
            shutil.move(file_path, new_file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create Folders for each file in the given directory')
    parser.add_argument('directory_path', type=str,
                        help='Path to directory containing files.')
    args = parser.parse_args()

file_folder_creator(args.directory_path)
