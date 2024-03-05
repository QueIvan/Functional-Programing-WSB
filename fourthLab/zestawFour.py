
def exponent_factory(exponent):
    return lambda x: x ** exponent

if __name__ == "__main__":
    square = exponent_factory(2)
    print(square(4))
