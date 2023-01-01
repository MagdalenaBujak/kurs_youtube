import random

los1 = random.randint(1,10)
los2 = random.randint(1,10)

pytanie = input(f"podaj wynik mnożenia {los1} * {los2}: ")
odp = los1 * los2


print(f"odpowiedź użytkownika to:{pytanie}")
print(f"odpowiedź komputera to:{odp}")


