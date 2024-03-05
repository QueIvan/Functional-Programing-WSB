
from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

if __name__ == "__main__":
    print(generate_permutations([1, 2, 3]))
