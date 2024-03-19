if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square = lambda x: x*x
    print(list(map(square, values)))
