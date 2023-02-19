import random

listaDobre = []
listaZle = []

for i in range(5):
    liczba1 = random.randint(1, 10)
    liczba2 = random.randint(1, 10)
    znak = random.randint(1, 3)

    if znak == 1:
        wynik1 = liczba1 + liczba2
        pytanie = int(input(f"podaj wynik {liczba1} + {liczba2}: "))
        if pytanie == wynik1:
            listaDobre.append(pytanie)
        elif pytanie != wynik1:
            listaZle.append(pytanie)
    if znak == 2:
        wynik2 = liczba1 - liczba2
        pytanie = int(input(f"podaj wynik {liczba1} - {liczba2}: "))
        if pytanie == wynik2:
            listaDobre.append(pytanie)
        elif pytanie != wynik2:
            listaZle.append(pytanie)
    if znak == 3:
        wynik3 = liczba1 * liczba2
        pytanie = int(input(f"podaj wynik {liczba1} * {liczba2}: "))
        if pytanie == wynik3:
            listaDobre.append(pytanie)
        elif pytanie != wynik3:
            listaZle.append(pytanie)

print(f"lista poprawnych odpowiedzi:", listaDobre)
print(f"lista błędnych odpwiedzi:", listaZle)




