def lazy_evaluation():
    num = 1
    while True:
        yield num
        num += 1


if __name__ == "__main__":
    generator = lazy_evaluation()

    for _ in range(5):
        print(next(generator))

    for _ in range(5):
        print(next(generator))
