import os
import shutil


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def copy_files_to_single_location(source_folder, destination_folder, file_extensions):
    """
    Copy files with specific extensions from the source folder to the destination folder without creating subfolders.

    Parameters:
    source_folder (str): The source folder path.
    destination_folder (str): The destination folder path.
    file_extensions (list): List of file extensions to copy.
    """
    for file_name in os.listdir(source_folder):
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)
        if os.path.isfile(source_file) and any(
            file_name.lower().endswith(ext) for ext in file_extensions
        ):
            shutil.copy2(source_file, destination_file)
            print(f"Copied {source_file} to {destination_file}")


def find_and_copy_files(
    source_dir,
    destination_dir,
    folder_name_keyword="",
    file_extensions=[".jpg", ".jpeg", ".png", ".gif"],
):
    """
    Traverses a folder and subfolders, finds all folders with a specific keyword in the folder name,
    and copies the files with specific extensions from those folders to another specified location.

    Parameters:
    source_dir (str): The source directory to traverse.
    destination_dir (str): The destination directory where the contents will be copied.
    folder_name_keyword (str): The keyword to search for in folder names. Default is an empty string "".
    file_extensions (list): List of file extensions to copy. Default is common image file extensions.
    """
    create_directory_if_not_exists(destination_dir)

    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            if folder_name_keyword.lower() in dir_name.lower():
                source_folder = os.path.join(root, dir_name)
                copy_files_to_single_location(
                    source_folder, destination_dir, file_extensions
                )


if __name__ == "__main__":
    source_directory = "source/path/"
    destination_directory = f"{source_directory}destination/"
    find_and_copy_files(source_directory, destination_directory)
