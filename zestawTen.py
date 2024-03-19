def infiniteTwo():
    num = 0
    while True:
        yield num
        num += 2


if __name__ == '__main__':
    generator = infiniteTwo()
    print(next(generator))
    print(next(generator))
