
def sum_of_squares_of_odds(lst):
    return sum(x**2 for x in lst if x % 2 != 0)

if __name__ == "__main__":
    print(sum_of_squares_of_odds([1, 2, 3, 4, 5]))
