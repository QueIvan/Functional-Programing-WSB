from functools import reduce

if __name__ == '__main__':
    data = [1, 2, 3, 32, 5, 6]
    print(reduce(lambda a, b: a if a > b else b, data))
