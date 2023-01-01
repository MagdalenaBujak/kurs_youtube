liczba1 = int(input("podaj liczbę:"))
liczba2 = int(input("podaj liczbę:"))
liczba3 = int(input("podaj liczbę:"))
liczba4 = int(input("podaj liczbę:"))
liczba5 = int(input("podaj liczbę:"))
liczba6 = int(input("podaj liczbę:"))

minimalna = liczba1
maksymalna = liczba1

if liczba2 > maksymalna:
    maksymalna = liczba2
if liczba2 < minimalna:
    minimalna = liczba2
if liczba3 > maksymalna:
    maksymalna = liczba3
if liczba3 < minimalna:
    minimalna = liczba3
if liczba4 > maksymalna:
    maksymalna = liczba4
if liczba4 < minimalna:
    minimalna = liczba4
if liczba5 > maksymalna:
    maksymalna = liczba5
if liczba5 < minimalna:
    minimalna = liczba5
if liczba6 > maksymalna:
    maksymalna = liczba6
if liczba6 < minimalna:
    minimalna = liczba6

print(f"min liczba to {minimalna}, a max liczba to {maksymalna}")

