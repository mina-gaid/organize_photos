import os
import shutil
from datetime import datetime

def organize_media(source_dir, dest_dir):
    # Traverse the source directory and identify all photos and videos
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Extract the date taken metadata from each media file
            date_taken = datetime.fromtimestamp(os.path.getmtime(file_path))
            year = date_taken.year
            month = date_taken.strftime('%B')
            # Create a directory structure in the destination directory based on the date taken
            year_dir = os.path.join(dest_dir, str(year))
            month_dir = os.path.join(year_dir, month)
            if not os.path.exists(year_dir):
                os.makedirs(year_dir)
            if not os.path.exists(month_dir):
                os.makedirs(month_dir)
            # Move the media files from the source directory to the destination directory and organize them accordingly
            shutil.move(file_path, month_dir)

if __name__ == '__main__':
    source_dir = input('Enter the source directory: ')
    dest_dir = input('Enter the destination directory: ')
    organize_media(source_dir, dest_dir)
