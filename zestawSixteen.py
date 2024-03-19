def compose(f, g):
    def h(x):
        return f(g(x))
    return h


def double(x):
    return x * 2


def square(x):
    return x ** 2


if __name__ == "__main__":
    comp = compose(double, square)
    print(comp(10))
