liczba = input("podaj liczbę: ")

slownik = {
    "0" : "zero",
    "1" : "jeden",
    "2" : "dwa",
    "3" : "trzy",
    "4" : "cztery",
    "5" : "pięć",
    "6" : "sześć",
    "7" : "siedem",
    "8" : "osiem",
    "9" : "dziewięć"
}


for i in range(len(liczba)):
    print(slownik[liczba[i]])
