pierwsza_liczba = float(input(f"Podaj pierwsza liczbe: "))
znak = input(f"Co chcesz zrobić? +, -, *, / : ")
druga_liczba = float(input(f"Podaj druga liczbe: "))

if znak == "+":
    wynik = pierwsza_liczba + druga_liczba
    print(wynik)
elif znak == "-":
    wynik = pierwsza_liczba - druga_liczba
    print(wynik)
elif znak == "*":
    wynik = pierwsza_liczba * druga_liczba
    print(wynik)
elif znak == "/":
    wynik = pierwsza_liczba / druga_liczba
    print(wynik)
else:
    print("Oj tego znaku nie obslugujemy! :(")