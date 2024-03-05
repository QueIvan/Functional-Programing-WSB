
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6]
    squares = [square for n in numbers if (square := n * n) > 10]
    print(squares)
