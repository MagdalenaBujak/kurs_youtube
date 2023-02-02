import random

lista1 = []
lista2 = []

for i in range(10):
    liczba = random.randint(1, 10)
    lista1.append(liczba)
for x in lista1:
    if lista1.count(x) == 1:
        lista2.append(x)






print(lista1)
print(lista2)




