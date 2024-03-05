
def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            total += item
    return total

if __name__ == "__main__":
    print(recursive_sum([1, 2, [3, 4], [5, [6, 7]]]))
