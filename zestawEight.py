
def partition_list(lst, condition):
    return [x for x in lst if condition(x)], [x for x in lst if not condition(x)]

if __name__ == "__main__":
    print(partition_list([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
