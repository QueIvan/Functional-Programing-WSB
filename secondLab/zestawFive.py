
def is_palindrome(s):
    return (cleaned := s.lower().replace(" ", "")) == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("Kajak"))
