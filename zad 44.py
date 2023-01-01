liczba1 = float(input("podaj pierwszą liczbę: "))
operacja = input("wpisz operator:")
liczba2 = float(input("podaj druga liczbę: "))

if operacja == "+":
    wynik = liczba1 + liczba2
    print(wynik)
elif operacja == "-":
    wynik = liczba1 - liczba2
    print(wynik)
elif operacja == "*":
    wynik = liczba1 * liczba2
    print(wynik)
else:
    print("niepoprawna operacja")


