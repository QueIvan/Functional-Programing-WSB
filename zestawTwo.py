def make_multiplier(y):
    def multiplier(x):
        return x * y
    return multiplier


if __name__ == '__main__':
    double = make_multiplier(5)
    print(double(2))
