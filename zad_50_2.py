# brak informacji o dodaniu kontaktu
# Usuwanie - wyszukac po nazwisku i usunac caly kontakt. plus info o usunieciu
# Zmiana - informacja o zmianie na koniec + wyszukanie po naziwsku

ksiazka = []

while True:
    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec:"))

    if menu == 1:
        imie = input("podaj imię: ")
        nazwisko = input("podaj nazwisko: ")
        tel = input("podaj numer telefonu: ")
        kontakt = [imie, nazwisko, tel]
        ksiazka.append(kontakt)
        print(f"kontakt: {imie}, {nazwisko}, {tel} został dodany do książki telefonicznej")
        # pytania: imie, nazwisko, telefon


    if menu == 2:
        for x in ksiazka:
            print(f"imie: {x[0]}, nazwisko: {x[1]}, numer tel: {x[2]}")
        # Imie:  .... Nazwisko: .... Telefon: .....


    if menu == 3:
        usun = input("podaj nazwisko które chcesz usunąć: ")
        for x in ksiazka:
            if usun == x[1]:
                ksiazka.remove(x)
                print(f"{usun} został usunięty z książki telefonicznej")
            else:
                print("podałeś niepoprawne dane")

    if menu == 4:
        pytanie = input("wpisz nazwisko, aby edytowac kontakt: :")
        for x in ksiazka:
            if pytanie == x[1]:
                x[1] = input("podaj nowe nazwisko: ")
                x[0] = input("podaj nowe imię: ")
                x[2] = input("podaj nowy nr tel: ")
                print(f"Dane zostały zaktualizowane na: {x[0]}, {x[1]}, {x[2]}")
            else:
                print("błędne dane")

        # pytania: nazwisko, noweImie, noweNazwisko, nowyTelefon

    if menu == 5:
        break

print(ksiazka)