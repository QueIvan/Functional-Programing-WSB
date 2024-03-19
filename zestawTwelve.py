from functools import partial


def multiplyByThree(x, y):
    return x * y


if __name__ == "__main__":
    newMethod = partial(multiplyByThree, 3)
    print(newMethod(5))
