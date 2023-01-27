import random

los = random.randint(1,100)

odp = -1
i = 0

while odp != los:
    i += 1
    odp = int(input("zgadnij liczbę z przedziału 1-100: "))
    if odp < los:
        print("podałeś za małą liczbę")
    elif odp > los:
        print("podałeś za dużą liczbę")
else:
    print("Gratulacje-trafiłeś!")

