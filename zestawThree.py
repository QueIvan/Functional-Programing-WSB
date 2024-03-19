def filter_even_numbers(numbers):
    return list(filter(lambda number: number % 2 == 0, numbers))


if __name__ == '__main__':
    print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
