import random

def mnozenie():
    i = 0
    while i < 5:
        liczba1 = random.randint(1, 10)
        liczba2 = random.randint(1, 10)
        while True:
            odp = liczba1 * liczba2
            print(f"ile to jest {liczba1} * {liczba2}")
            wynik = int(input("podaj wynik mnożenia:"))
            if odp == wynik:
                i += 1
                print("brawo!")
                break
            elif odp != wynik:
                print("spóbuj jeszcze raz")
                continue
mnozenie()




