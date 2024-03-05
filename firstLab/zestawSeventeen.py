import functools


def addFiveTo(val, add):
    return val + add


if __name__ == "__main__":
    comp = functools.partial(addFiveTo, 5)
    print(comp(10))
