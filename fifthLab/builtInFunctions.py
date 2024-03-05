if __name__ == '__main__':
    data = {'id': 0, 'name': "Test"}
    data_new = [1, 2, 3, 4, 5, 6]

    print(list(filter(lambda x: x != 5, data_new)))  # filter / list
    print(list(enumerate(data)))  # enumerate / list

    print(eval("data_new[3]+2"))  # eval

    print(pow(2, 2))  # pow

