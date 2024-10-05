import os
from PIL import Image


def tile_image(image_path: str, output_dir: str, tile_size: tuple[int, int]) -> list[str]:
    """
    Tile an image into smaller patches.

    Args:
        image_path (str): Path to the input image.
        output_dir (str): Directory to save the tiles.
        tile_size (tuple[int, int]): Size of each tile (width, height).

    Returns:
        List[str]: List of file paths to the saved tiles.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = Image.open(image_path)
    image_width, image_height = image.size
    tile_width, tile_height = tile_size

    tile_paths = []

    for i in range(0, image_width, tile_width):
        for j in range(0, image_height, tile_height):
            box = (i, j, i + tile_width, j + tile_height)
            tile = image.crop(box)
            tile_filename = f"{os.path.splitext(os.path.basename(image_path))[0]}_{i}_{j}.png"
            tile_path = os.path.join(output_dir, tile_filename)
            tile.save(tile_path)
            tile_paths.append(tile_path)

    return tile_paths


def tile_images_in_folder(input_dir: str, output_dir: str, tile_size: tuple[int, int]) -> None:
    """
    Tile all images in a folder into smaller patches.

    Args:
        input_dir (str): Directory containing the input images.
        output_dir (str): Directory to save the tiles.
        tile_size (tuple[int, int]): Size of each tile (width, height).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_dir, filename)
            tile_image(image_path, output_dir, tile_size)


if __name__ == "__main__":

    input_dir = os.getcwd()
    output_dir = input_dir
    width, height = 64, 64
    tile_size = (width, height)

    tile_images_in_folder(input_dir, output_dir, tile_size)
    print(f"Images in {input_dir} have been tiled and saved to {output_dir}")
