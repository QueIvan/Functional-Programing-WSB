
def filter_even_values(d):
    return {k: v for k, v in d.items() if v % 2 == 0}

if __name__ == "__main__":
    print(filter_even_values({'a': 1, 'b': 2, 'c': 3, 'd': 4}))
