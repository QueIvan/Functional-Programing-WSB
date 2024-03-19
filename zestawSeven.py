
def merge_dictionaries(*dicts):
    merged = {}
    for d in dicts:
        for k, v in d.items():
            merged[k] = merged.get(k, 0) + v
    return merged

if __name__ == "__main__":
    print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5, 'd': 6}))
