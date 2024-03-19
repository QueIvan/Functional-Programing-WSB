
def map_nested(lst, func):
    return [map_nested(x, func) if isinstance(x, list) else func(x) for x in lst]

if __name__ == "__main__":
    print(map_nested([1, 2, [3, 4], [5, [6, 7]]], lambda x: x * 2))
