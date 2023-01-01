wynik = input("chcesz policzyć pole wybierz 1, chcesz policzyć obwód wybierz 2: " )
a = float(input("podaj długość pierwszego boku prostokąta: "))
b = float(input("podaj długość drugiego boku prostokąta: "))

if wynik == "1":
    pole = a * b
    print(f"pole prostokąta wynosi: {pole}")
elif wynik == "2":
    obwod = 2 * a + 2 * b
    print(f"obwód prostokąta wynosi: {obwod}")

