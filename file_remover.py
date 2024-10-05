import os
import random
from typing import Union
from colorama import init, Fore


def get_image_files(
    folder_path: str, extensions: tuple[str, ...] = (".png", ".jpg", ".jpeg")
) -> list[str]:
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(extensions)
    ]


def delete_random_images(
    folder_path: str,
    num_images: Union[int, str],
    extensions: tuple[str, ...] = (".png", ".jpg", ".jpeg"),
) -> None:
    image_files = get_image_files(folder_path, extensions)

    if num_images == "all":
        num_images = len(image_files)
    elif isinstance(num_images, int) and num_images > len(image_files):
        print(f"Error: The folder only contains {len(image_files)} images.")
        return

    images_to_delete = (
        random.sample(image_files, num_images) if num_images != "all" else image_files
    )

    print_warning(
        f"WARNING: You are about to delete {num_images} images from '{folder_path}'. This action is irreversible."
    )
    print("The following images will be deleted:")
    for image in images_to_delete:
        print(image)

    print_warning(
        f"WARNING: You are about to delete {num_images} images from '{folder_path}'. This action is irreversible."
    )
    confirmation = input("Are you sure you want to proceed? Type 'yes' to confirm: ")
    if confirmation.lower() == "yes":
        for image in images_to_delete:
            os.remove(image)
        print(f"{num_images} images have been deleted.")
    else:
        print("Operation cancelled.")


def print_warning(message: str) -> None:
    init(autoreset=True)
    print(Fore.RED + message)


if __name__ == "__main__":
    folder_path = os.getcwd()
    num_images_input = "all"
    num_images = (
        int(num_images_input) if num_images_input.isdigit() else num_images_input
    )
    extensions = input(
        "Enter the file extensions to include (comma-separated, e.g., .png,.jpg,.jpeg): "
    ).split(",")

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        delete_random_images(folder_path, num_images, tuple(extensions))
    else:
        print("Error: The specified folder path does not exist or is not a directory.")
