ksiazka = []

while True:
    menu = int(input("1-dodaj, 2-pokaz, 3-usun, 4-zmien, 5-koniec:"))

    if menu == 1:
        imie = input("podaj imię: ")
        nazwisko = input("podaj nazwisko: ")
        tel = input("podaj numer telefonu: ")
        kontakt = [imie,nazwisko,tel]
        ksiazka.append(kontakt)
        # pytania: imie, nazwisko, telefon


    if menu == 2:
        for x in ksiazka:
            print(f"imie: {x[0]}, nazwisko: {x[1]}, numer tel: {x[2]}")
        # Imie:  .... Nazwisko: .... Telefon: .....


    if menu == 3:
        usun = int(input("co chcesz usunąć z listy: 4 - imię, 5- nazwisko, 6 - nr tel: "))

        if usun == 4:
            imi = input("podaj imie: ")
            kontakt.remove(imi)
            print(f"imię {imi} zostało usunięte z książki")
        elif usun == 5:
            naz = input("podaj nazwisko: ")
            kontakt.remove(naz)
            print(f"nazwisko {naz} zostało usunięte z książki")
        elif usun == 6:
             num = input("podaj numer tel:")
             kontakt.remove(num)
             print(f"numert tel {num} został usunięty z książki")
        else:
            print("błędne dane")

        # pytania: nazwisko


    if menu == 4:
        pytanie = input("wpisz imię które chcesz zmienić:")
        for x in ksiazka:
            if pytanie == x[0]:
                x[0] = input("podaj nowe imie: ")
                x[1] = input("podaj nowe nazwisko: ")
                x[2] = input("podaj nowy nr tel: ")
            else:
                print("błędne dane")

        # pytania: nazwisko, noweImie, noweNazwisko, nowyTelefon

    if menu == 5:
        break

print(ksiazka)