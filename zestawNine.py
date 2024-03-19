
def apply_to_tuple_list(lst, func):
    return [func(*t) for t in lst]

if __name__ == "__main__":
    print(apply_to_tuple_list([(1, 2), (3, 4)], lambda x, y: x + y))
