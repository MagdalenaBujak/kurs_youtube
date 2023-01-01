wynik = input(f"co chcesz polczyć? pole czy obwód?: ")

r = float(input("podaj promień koła: "))
pi = 3.1415

if wynik == "pole":
    pole = float(pi * (r * r))
    print(f"pole koła wynosi: {pole}")
elif wynik == "obwód":
    obwod = float((2 * pi) * r)
    print(f"Obwód koła wynosi: {obwod}")



