import random

lista1 = []
lista2 = []


for x in range(10):
    lista1.append(random.randint(1, 20))
    lista2.append(random.randint(1, 20))

max = 0

for x in lista1:
    for y in lista2:
        if y == x and y > max:
            max = y
        if x == y and x > max:
            max = x

print(f"lista1 {lista1}")
print(f"lista2 {lista2}")
print(f"największa wartość na obu listach to: {max}")