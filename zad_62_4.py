lista = []

while True:
    pytanie = int(input("podaj dowalną liczbę: "))

    if pytanie > 0:
        lista.append(pytanie)
    else:
        pytanie == 0
        break

x = len(lista)

while x > 1:

    for i in range(0, x-1):
        if lista[1] > lista[1 + 1]:
            lista[1], lista[1 +1] = lista[1 +1], lista[1]
    x -= 1

print(lista)


#lista.sort()
#print(lista)