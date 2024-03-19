
def most_frequent_element(lst):
    return max(set(lst), key=lst.count)

if __name__ == "__main__":
    print(most_frequent_element([1, 2, 3, 1, 2, 1, 2, 2]))
