
from itertools import groupby


def group_by_parity(numbers):
    return {k: list(g) for k, g in groupby(sorted(numbers), key=lambda x: x % 2)}


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    print(group_by_parity(numbers))
