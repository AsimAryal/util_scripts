from pathlib import Path
import shutil
import random
import math


def get_image_files(folder_path: Path) -> list[Path]:
    image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff")
    return [f for f in folder_path.iterdir() if f.suffix.lower() in image_extensions]


def create_val_folder(
    folder_path: Path, percent: float = 0, exact_number: int = 0
) -> Path:
    """Create a validation folder inside the given folder."""
    folder_name_suffix = (
        f"{str(percent)}_percent" if percent else f"{str(exact_number)}"
    )
    val_folder_path = folder_path / f"{folder_path.name}_val_{folder_name_suffix}"
    val_folder_path.mkdir(exist_ok=True)
    return val_folder_path


def transfer_images(
    folder_path: Path, percent: float = 0, exact_number: int = 0, move: bool = True
) -> None:
    """Move or copy percent% of images or exact number of from the folder to its validation folder."""
    image_files = get_image_files(folder_path)
    if not image_files:
        print(f"No image files found in '{folder_path}'.")
        return

    val_folder_path = create_val_folder(
        folder_path, percent=percent, exact_number=exact_number
    )
    num_images_to_transfer = (
        math.ceil(len(image_files) * (percent / 100))
        if exact_number == 0
        else exact_number
    )
    if num_images_to_transfer > len(image_files):
        print(
            "Number of files to transfer is greater than total number of files in source directory."
        )
        return

    images_to_transfer = random.sample(image_files, num_images_to_transfer)

    for image in images_to_transfer:
        if move:
            shutil.move(image, val_folder_path / image.name)
        else:
            shutil.copy(image, val_folder_path / image.name)

    print(f"Total image files in '{folder_path}' at the start: {len(image_files)}")
    print(
        f"Number of files {'moved' if move else 'copied'} to '{val_folder_path}': {num_images_to_transfer}"
    )
    print("Files transferred:")
    [print(image.name) for image in images_to_transfer]


def transfer_images_in_subfolders(
    parent_path: Path, percent: float = 0, exact_number: int = 0, move: bool = True
) -> None:
    """Move or copy percent% of images in each sub-folder of the parent folder."""
    for folder_path in parent_path.iterdir():
        if folder_path.is_dir():
            transfer_images(folder_path, percent, exact_number, move)


if __name__ == "__main__":
    folder_path = Path("/folder_path/")
    # Example usage for a single folder
    transfer_images(folder_path=folder_path, percent=0, exact_number=5, move=False)

    # Example usage for multiple sub-folders
    transfer_images_in_subfolders(
        parent_path=Path("/parent_folder"), percent=0.5, move=False
    )
