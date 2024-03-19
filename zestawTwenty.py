def analyze_data(data):
    match data:
        case []:
            print("Lista jest pusta.")
        case [x]:
            print(f"Jedyny element listy to: {x}")
        case [x, *rest]:
            print(f"Pierwszy element listy to: {x}")
            print(f"Pozostałe elementy listy to: {rest}")
        case _:
            print("Nieznany typ danych.")


if __name__ == "__main__":
    analyze_data([])
    analyze_data([1])
    analyze_data([1, 2, 3, 4])
    analyze_data((1, 2, 3))
