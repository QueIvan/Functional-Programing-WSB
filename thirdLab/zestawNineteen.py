
def check_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

if __name__ == "__main__":
    print(check_anagrams("listen", "silent"))
