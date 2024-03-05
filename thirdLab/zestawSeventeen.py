
def capitalize_all_words(s):
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == "__main__":
    print(capitalize_all_words("hello world python"))
