import random

lista = []
duplikaty = set()

for x in range(10):
    a = random.randint(1, 10)
    lista.append(a)

for i in lista:
    if lista.count(i) != 1:
        duplikaty.add(i)

print(lista)
print(f"duplikaty:", duplikaty)
