
def remove_whitespace(strings):
    return [s.replace(" ", "") for s in strings]

if __name__ == "__main__":
    print(remove_whitespace([" hello ", " world ", " python "]))
