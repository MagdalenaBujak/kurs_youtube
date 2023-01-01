import random

los1 = random.randint(1,10)
los2 = random.randint(1,10)

pytanie = int(input("jaki jest wynik mnożenia wylosowanych libcz?: "))
odp = los1 * los2

print("odpowiedz użytkownika:", pytanie)
print("poprawna odpowiedź: ", odp)

