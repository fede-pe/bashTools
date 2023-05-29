import os
import shutil
import glob


def copy_file_with_counter(source_file_regex, destination_folder, basename):
    # Get the list of files in the source directory
    source_files = os.listdir()

    # Filter the files based on the provided regular expression
    matching_files = glob.glob(source_file_regex)

    for source_file in matching_files:
        # Extract the basename and extension of the source file
        _, extension = os.path.splitext(source_file)
        counter = 1

        # Generate the destination file path
        destination_file = os.path.join(destination_folder, f"{basename}{extension}")

        # Check if the destination file already exists
        while os.path.exists(destination_file):
            # Append the counter to the basename and generate a new destination file path
            basename_with_counter = f"{basename}_{counter}"
            destination_file = os.path.join(destination_folder, f"{basename_with_counter}{extension}")
            counter += 1

        # Copy the file to the destination folder
        shutil.copy2(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}'.")


# Take source file regex and destination folder as input
source_file_regex = input("Enter the regular expression for the source file(s): ")
destination_folder = input("Enter the path of the destination folder: ")
basename = input("Enter the basename of the copied files: ")

copy_file_with_counter(source_file_regex, destination_folder, basename)
