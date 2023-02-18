import os
import shutil
import exifread
import calendar

# function to get the date taken from the file metadata
def get_date_taken(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        date_tag = tags.get('EXIF DateTimeOriginal')
        if date_tag:
            date_str = str(date_tag)
            year_month = date_str[:7].replace(':', '-')
            year, month = year_month.split('-')
            month_name = calendar.month_name[int(month)]
            month_dir = os.path.join(year, month_name.title())
            return month_dir
        else:
            return None

# get the directory path from the user
dir_path = input("Enter the directory path: ")

# loop through all files in the directory
for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)

    # skip directories
    if os.path.isdir(file_path):
        continue

    # get the month directory for image or video files
    if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.mov', '.mp4', '.avi')):
        month_dir = get_date_taken(file_path)
        if month_dir:
            year_month_dir = os.path.join(dir_path, month_dir)
            if not os.path.exists(year_month_dir):
                os.makedirs(year_month_dir)
            shutil.move(file_path, os.path.join(year_month_dir, file_name))
            print("Moved {} to {}".format(file_name, year_month_dir))
            continue

    # move other files to a "Unknown" directory
    unknown_dir = os.path.join(dir_path, "Unknown")
    if not os.path.exists(unknown_dir):
        os.mkdir(unknown_dir)
    shutil.move(file_path, os.path.join(unknown_dir, file_name))
    print("Moved {} to {}".format(file_name, unknown_dir))
