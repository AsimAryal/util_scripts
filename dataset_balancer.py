import random
from collections import Counter


def balance_dataset(data: list[tuple[str, int]], strategy: str = "oversample") -> list[tuple[str, int]]:
    """
    Balance the dataset by oversampling or undersampling.

    Args:
        data (list[tuple[str, int]]): List of tuples where each tuple contains (image_path, label).
        strategy (str): Strategy to balance the dataset, either 'oversample' or 'undersample'.
        'oversample' duplicates random samples to balance.

    Returns:
        list[tuple[str, int]]: Balanced dataset.
    """

    label_counts: dict[int, int] = Counter(label for _, label in data)
    max_count: int = max(label_counts.values())
    min_count: int = min(label_counts.values())

    balanced_data: list[tuple[str, int]] = []

    if strategy == "oversample":
        for label in label_counts:
            samples = [item for item in data if item[1] == label]
            balanced_data.extend(samples)
            balanced_data.extend(random.choices(samples, k=max_count - len(samples)))
    elif strategy == "undersample":
        for label in label_counts:
            samples = [item for item in data if item[1] == label]
            balanced_data.extend(random.sample(samples, min_count))
    else:
        raise ValueError("Strategy must be either 'oversample' or 'undersample'")

    return balanced_data


# Example usage
if __name__ == "__main__":
    # Example dataset: list of (image_path, label)
    dataset = [
        ("image1.jpg", 0),
        ("image2.jpg", 0),
        ("image3.jpg", 1),
        ("image4.jpg", 1),
        ("image5.jpg", 1),
        ("image6.jpg", 2),
    ]

    balanced_dataset = balance_dataset(dataset, strategy="oversample")
