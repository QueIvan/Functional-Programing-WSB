
from itertools import product


def two_element_combinations(elements):
    return [pair for pair in product(elements, repeat=2)]


if __name__ == "__main__":
    elements = ['A', 'B', 'C']
    print(two_element_combinations(elements))
