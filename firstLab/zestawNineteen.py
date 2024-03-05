def tuple_operations(tup):
    print("Długość krotki:", len(tup))

    print("Elementy krotki:")
    for item in tup:
        print(item)

    value = 3
    if value in tup:
        print(f"Wartość {value} występuje w krotce.")
    else:
        print(f"Wartość {value} nie występuje w krotce.")


if __name__ == "__main__":
    krotka = (1, 2, 3, 4, 5)
    tuple_operations(krotka)
