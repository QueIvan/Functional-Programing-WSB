
def filter_long_words(strings):
    avg_length = sum(len(s) for s in strings) / len(strings)
    return [s for s in strings if len(s) > avg_length]

if __name__ == "__main__":
    print(filter_long_words(["hello", "world", "Python", "is", "awesome"]))
