
def apply_function(lst, func):
    return [func(x) for x in lst]

if __name__ == "__main__":
    print(apply_function([1, 2, 3, 4], lambda x: x * 2))
