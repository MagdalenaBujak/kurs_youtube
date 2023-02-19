import random

lista = []

for i in range(10):
    a = random.randint(1, 100)
    lista.append(a)

najmniejsza = 1
najwieksza = 1

for x in lista:
    if najmniejsza == 1 or najmniejsza > x:
        najmniejsza = x
    if najwieksza == 1 or najwieksza < x:
        najwieksza = x

print(lista)

print(f"najmniejsza liczba to: {najmniejsza}")
print(f"największa liczba to: {najwieksza}")



