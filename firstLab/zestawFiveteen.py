def add(a):
    def inner(b):
        return a + b

    return inner


if __name__ == "__main__":
    adder = add(3)
    print(adder(3))
