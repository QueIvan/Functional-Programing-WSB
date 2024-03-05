
def custom_sort(lst, key_func):
    return sorted(lst, key=key_func)

if __name__ == "__main__":
    print(custom_sort(["banana", "apple", "cherry"], key_func=len))
