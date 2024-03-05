SETUP_INDEX = 0


def moveIndexBy(value):
    global SETUP_INDEX
    SETUP_INDEX += value


def innerScopeIndex():
    SETUP_INDEX = 12
    print(SETUP_INDEX)


if __name__ == '__main__':
    moveIndexBy(3)
    print(SETUP_INDEX)
    innerScopeIndex()
    print(SETUP_INDEX)