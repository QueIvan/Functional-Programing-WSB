
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
