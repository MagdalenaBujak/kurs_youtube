liczba = input("Podaj liczbe: ")

# for i in liczba:
#     if i == "1":
#         print("jeden")
#     elif i == "2":
#         print("dwa")
#     elif i == "3":
#         print("trzy")
#     elif i == "4":
#         print("cztery")
#     elif i == "5":
#         print("piec")


slownik = {
    "1":"jeden",
    "2":"dwa",
    "3":"trzy",
    "4":"cztery",
    "5":"piec"
}

for i in range(len(liczba)):
    print(slownik[liczba[i]])