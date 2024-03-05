
def split_list(lst, length):
    return [lst[i:i+length] for i in range(0, len(lst), length)]

if __name__ == "__main__":
    print(split_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
