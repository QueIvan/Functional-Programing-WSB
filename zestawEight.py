from functools import reduce

if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(reduce(lambda x, y: x+y, values))

