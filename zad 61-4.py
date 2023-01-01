lista = []

for x in range(5):
    lista.append(int(input("podaj liczbę: ")))

suma = 0

for x in lista:
    if x % 2 == 0:
        suma = suma + x
        print(suma)

test2
