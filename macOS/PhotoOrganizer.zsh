#!/bin/zsh

# Prompt user for source and destination directories
echo "Enter the source directory: "
read source_dir
echo "Enter the destination directory: "
read dest_dir

# Traverse the source directory and identify all photos and videos
for file in ${(0)$(find $source_dir -type f)}; do
    # Extract the date taken metadata from each media file
    date_taken=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" $file)
    year=$(date -j -f "%Y-%m-%d %H:%M:%S" "$date_taken" "+%Y")
    month=$(date -j -f "%Y-%m-%d %H:%M:%S" "$date_taken" "+%B")
    # Create a directory structure in the destination directory based on the date taken
    year_dir="$dest_dir/$year"
    month_dir="$year_dir/$month"
    mkdir -p $month_dir
    # Move the media files from the source directory to the destination directory and organize them accordingly
    mv $file $month_dir
done
