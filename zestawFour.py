def function_a(other_one):
    print("Czasami trzeba zrobic ", other_one)


def function_b(value):
    return f"coś {value}"


if __name__ == '__main__':
    function_a(function_b("szalonego"))