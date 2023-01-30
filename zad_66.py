import random

def dzialania(dane):
    minimalna = dane
    maksymalna = dane
    for x in dane:
        if x > maksymalna:
            maksymalna = x
        elif x < minimalna:
            minimalna = x

    parzyste = []
    nieparzyste = []

    for x in dane:
        if x % 2 == 0:
            parzyste.append(x)
        else:
            nieparzyste.append(x)

    suma = 0

    for x in dane:
        suma += x
        srednia = suma/(len(dane))

    return minimalna, maksymalna, parzyste, nieparzyste, srednia

lista = []

for x in range(10):
    lista.append(random.randint(1, 10))

print(lista)

wynik = dzialania(lista)

print(wynik)