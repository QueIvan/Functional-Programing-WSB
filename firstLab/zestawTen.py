def read_line_by_line(file_name):
    with open(file_name, "r") as infile:
        for line in infile:
            yield line


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    for line in read_line_by_line("lorem.txt"):
        print(line)

    fibonacci_gen = fibonacci()

    for _ in range(10):
        print(next(fibonacci_gen))
