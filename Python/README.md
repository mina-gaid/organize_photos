# Organize Photos by Date

This Python script organizes photo files in a directory by their date taken or date modified. The script creates directories for each year and month, and moves image and video files to their corresponding year and month directories. Other files are moved to an "Unknown" directory.

## Getting Started

1. Install the required dependencies by running the following command:

```
pip install exifread
```

2. Download the script to a directory of your choice.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script by typing the following command and pressing Enter:

```
python organize_photos.py
```

5. Enter the directory path when prompted.

## How it works

The script uses the `exifread` module to extract the date taken from the metadata of image and video files. The date taken is used to create year and month directories, and the photo files are moved to their corresponding directories.

For other files, the script creates an "Unknown" directory and moves them there.

## Customization

You can customize the script to use the date modified instead of date taken by changing the `get_date_taken` function to use the `os.path.getmtime` function.

You can also customize the photo file extensions that the script looks for by modifying the `photo_extensions` tuple.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
