podstawa = int(input("podaj liczbę: "))
wykladnik = int(input("podaj potęgę: "))

wynik = 1

for x in range(wykladnik):
    wynik = wynik * podstawa
print(wynik)

