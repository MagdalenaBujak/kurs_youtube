from random import randint

los = randint(1,10)
odp = -1
i = 0

print("zgadnij liczbę w przedziale 1-10")
while odp != los:
    i += 1
    odp = int(input("podaj liczbę: "))
    if odp > los:
        print("niestety podana liczba jest mniejsza od Twojej")
    elif odp < los:
        print("niestety podana liczba jest większa od Twojej")
print("brawo! odgadłeś liczbę za", i, "razem")
