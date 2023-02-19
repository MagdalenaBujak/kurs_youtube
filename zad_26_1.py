import random

lista1 = []
lista2 = []
elementyWspolne = []

for x in range(10):
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    lista1.append(a)
    lista2.append(b)

for x in lista1:
    for y in lista2:
        if x == y:
            elementyWspolne.append(y)



print(lista1)
print(lista2)
print(f"elementy wspólne dla obu list", elementyWspolne)