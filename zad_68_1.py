class Pracownicy():

    def __init__(self, imie, nazwisko, email, tel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.tel = tel


lista_prac = []

while True:
    menu = int(input("co chcesz zrobić: 1 - dodaj, 2 - pokaz, 3 - usuń, 4- zmień, 5 - koniec: "))

    if menu == 1:
        imie = input("podaj imię: ")
        nazwisko = input("podaj nazwisko: ")
        email = input("podaj email: ")
        tel = input("podaj nr tel: ")

        pracownik = Pracownicy(imie, nazwisko, email, tel)
        lista_prac.append(pracownik)

        print(f"Pracownik {pracownik.imie}, {pracownik.nazwisko}, {pracownik.email}, {pracownik.tel} został dodany")


    elif menu == 2:
        for x in lista_prac:
            print(f"{x.imie}, {x.nazwisko}, {x.email}, {x.tel}")


    elif menu == 3:
        usun = input("podaj nazwisko pracownika, którego chcesz usunąć: ")
        sprawdzenie = False
        for x in lista_prac:
            if usun == x.nazwisko:
                lista_prac.remove(x)
                print(f"pracownik {usun} został usunięty z listy")
                sprawdzenie = True
        if sprawdzenie == False:
            print("brak pracownika na liście")

    elif menu == 4:
        pytanie = input("podaj nzawisko które chcesz zmienić: ")

        for x in lista_prac:
            if pytanie == x.nazwisko:
                x.imie = input("podaj nowe imie: ")
                x.nazwisko = input("podaj nowe nazwisko:")
                x.email = input("podaj nowy email: ")
                x.tel = input("podaj nowy nr tel: ")
                print(f" dane zostały zaktualizowane {x.imie}, {x.nazwisko}, {x.email}, {x.tel}")

            else:
                print("błędne dane")

    elif menu == 5:
        break










