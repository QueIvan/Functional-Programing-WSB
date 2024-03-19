def factorial(val):
    return val * factorial(val-1) if not val == 0 else 1


if __name__ == "__main__":
    print(factorial(5))
