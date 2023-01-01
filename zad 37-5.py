import random

los1 = random.randint(1,10)
los2 = random.randint(1,10)

pytanie = int(input(f"podaj wynik mnożenia {los1} * {los2}: "))


if pytanie == los1 * los2:
    print("Brawo! podałeś prawidłową odpowiedź")
elif pytanie != los1 * los2:
    print("Błąd- spróbuj jeszcze raz")

