def get_only_even(data):
    return list(filter(lambda x: x % 2 == 0, data))


if __name__ == '__main__':
    print(get_only_even([1, 2, 3, 4, 5, 6]))
    print((lambda a, b: a * b)(2, 3))
