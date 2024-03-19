def sortByLength(values):
    return list(sorted(values, key=lambda x: len(x)))


if __name__ == "__main__":
    strings = ['e', 'Uxw', 'ZmPN', 'lmRqR', 'iljTY', 'XvWQpK', 'AjxRcCq', 'mHXonRq', 'sUQYzLSW', 'qNPrxudQT']
    print(sortByLength(strings))
