import os
import shutil
from datetime import datetime
import argparse

def organize_files(source_directory):
    # List all files in the source directory
    files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]

    for file_name in files:
        file_path = os.path.join(source_directory, file_name)

        # Get file modified timestamp
        creation_timestamp = os.path.getmtime(file_path)

        # Convert timestamp to datetime object
        creation_date = datetime.utcfromtimestamp(creation_timestamp).date()

        # Create subfolder based on creation date
        subfolder = os.path.join(source_directory, str(creation_date))
        os.makedirs(subfolder, exist_ok=True)

        # Move the file to the subfolder
        destination_path = os.path.join(subfolder, file_name)
        shutil.move(file_path, destination_path)

        print(f"Moved {file_name} to {subfolder}")

def main():
    parser = argparse.ArgumentParser(description='Organize files based on modification date.')
    parser.add_argument('source_directory', type=str, help='Path to the source directory')

    args = parser.parse_args()
    source_directory = args.source_directory

    organize_files(source_directory)

if __name__ == "__main__":
    main()
