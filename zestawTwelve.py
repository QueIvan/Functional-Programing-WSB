
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))
