import re
from pathlib import Path


def create_dir_if_not_exists(path: Path) -> None:
    """Creates a directory if it does not exist.

    Parameters:
    path (Path): The path where the directory should be created.
    """

    if not path.exists():
        path.mkdir(parents=True)
        print(f"Experiment Directory {path} created.")
    else:
        print(f"Directory {path} already exists.")


def get_next_exp_num(path: Path, pattern: str = r"exp_(\d+)") -> int:
    """Finds the next experiment number to run based on previous experiment folders.
    Parameters:
    path (Path): Path to check previous experiment numbers.
    pattern (str): Pattern of folder naming convention to match.

    Returns:
    int: The next experiment number.
    """
    exp_nums = [
        int(match.group(1))
        for file in path.iterdir()
        if (match := re.match(pattern, file.name))
    ]

    return max(exp_nums, default=0) + 1


if __name__ == "__main__":
    # Example usage:
    results_dir = Path.cwd()
    exp_number = get_next_exp_num(results_dir)
    print(f"Experiment number: {exp_number}")
    output_dir = results_dir / f"exp_{exp_number}"
    create_dir_if_not_exists(output_dir)
