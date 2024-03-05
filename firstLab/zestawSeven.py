def pow_this(number):
    return number*number


def add_five(number):
    return number+5


def add_number(number, second):
    return number+second


def apply_two(data):
    data = map(pow_this, data)
    data = map(add_five, data)
    return list(data)


def do_function(functions, arguments):
    for f, v in zip(functions, arguments):
        print(f(*v) if isinstance(v, tuple) else f(v))


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6]
    do_function([pow_this, add_five, add_number], [5, 10, (10, 15)])

