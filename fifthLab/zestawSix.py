def starting_with_a(data):
    return list(filter(lambda x: x[0] == 'a', data))


def pow_list(data):
    return list(map(lambda x: x*x, data))


if __name__ == '__main__':
    print(starting_with_a(["ala", "mara", "tara"]))
    print(pow_list([1, 2, 3, 4, 5]))
