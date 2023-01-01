import random

liczba1 = random.randint(1,9)
liczba2 = random.randint(1,9)
znak = random.randint(1,3)

wynik1 = liczba1 + liczba2
wynik2 = liczba1 - liczba2
wynik3 = liczba1 * liczba2

if znak == 1:
    losowanie = (f"ile to jest {liczba1} + {liczba2} ?")
    print(losowanie)
elif znak == 2:
    losowanie = (f"ile to jest {liczba1} - {liczba2}?")
    print(losowanie)
elif znak == 3:
    losowanie = (f"ile to jest {liczba1} * {liczba2}?")
    print(losowanie)

pytanie = int(input(f"podaj wynik działania: "))

if pytanie == wynik1:
    print("Brawo! poprawna odpowiedź")
elif pytanie == wynik2:
    print("Brawo! poprawna odpowiedź")
elif pytanie == wynik3:
    print("Brawo! poprawna odpowiedź")
else:
    print("Błąd! Spróbuj jeszcze raz")
