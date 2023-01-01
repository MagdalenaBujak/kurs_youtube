figura = input("wybierz co chcesz policzyć: 1- prostokąt, 2 - trójkąt: ")

if figura == "1":
    a = float(input("podaj długość boku a: "))
    b = float(input("podaj dłigość boku b: "))
    pole = a * b
    print(f"pole prostokąta wynosi:{pole}")
elif figura == "2":
    podstawa = float(input("podaj długość podstawy: "))
    wysokosc = float(input("podaj wysokość trójkąta: "))
    poleTr = 0.5 * podstawa * wysokosc
    print(f"pole trójkąta wynosi: {poleTr}")