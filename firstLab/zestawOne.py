def apply_twice(callback, value):
    return callback(callback(value))


if __name__ == '__main__':
    print(apply_twice(lambda x: x*2, 5))
