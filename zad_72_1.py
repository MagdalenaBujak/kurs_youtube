sklep = {"chleb": 3.50, "sok": 6.00, "cukier": 4.25}
koszyk = {}

while (True):

    print("Witaj w sklepie")
    menu = input("D-dodaj, P-pokaz, U-usun, K-kasa/koniec ??  ").upper()

    if (menu == "D"):
        produkt = input("co chcesz kupić:")
        if produkt in sklep:
            ilosc = int(input("podaj ilość:"))

            if produkt in koszyk:
                koszyk[produkt] += ilosc
            else:
                koszyk[produkt] = ilosc
        else:
            print("niestety w sklepie brak wybranego przez ciebie produktu")

        # pytania: produkt, ilosc (pytamy wtedy kiedy jest produkt w sklepie)
        # sok - 2 i dodajemy kolejne 4 soki to w koszyku ma byc ich 6
        pass

    elif (menu == "P"):
        for x in koszyk:
            print(f"produkty {x}, ilość {koszyk[x]}")
        pass

    elif (menu == "U"):
        produkt_usun = input("co chcesz usunąć z koszyka?:")
        if produkt_usun in koszyk:
            ilosc = koszyk[produkt_usun]
            ile_usun = int(input("podaj ilość: "))

            if ilosc > ile_usun:
                koszyk[produkt_usun] -= ile_usun
            elif ilosc == ile_usun:
                koszyk.pop(produkt_usun)
            elif ilosc < ile_usun:
                print("podałeś za dużą ilość")



        # pytania: produkt, ilosc (pytamy wtedy kiedy produkt jest w koszyku)
        # jezeli ilosc w koszyku > ilosci usuwanej - to zmniejszamy ilosc tego produktu w koszyku
        # jezeli ilosc w koszyku == ilosci usuwanej - to usuwamy caly produkt z koszyka, nie trzymamy stanow zerowych
        # jezeli ilosc w koszyku < ilosci usuwanej - to dajemy komunikat (Brak wystarczajace ilosci w koszyku)

        pass

    elif (menu == "K"):
        print("Paragon")
        razem = 0
        for x in koszyk:
            ilosc_wkoszyku = koszyk[x]
            wartosc = ilosc_wkoszyku * sklep[x]
            razem = wartosc + razem
            print(f"produkty: {x}, ilość: {koszyk[x]}, cena: {sklep[x]}, wartość: {wartosc}")
            print(f"razem do zapłaty: {razem} PLN")

            if razem >= 10.00:
                rabat = razem * 0.1
                kwota = razem - rabat
                print(f"dostałeś rabat wysokości : {rabat}")
                print(f"kwota z uwzględnieniem rabatów to: {kwota} PLN")
            else:
                print(f"do rabatu brakuje ci jeszcze {10 - razem}")


        # Produkt: ..... Ilosc: ..... Cena:..... Wartosc: ....
        # Produkt: ..... Ilosc: ..... Cena:..... Wartosc: ....
        # RAZEM DO ZAPLATY :...... PLN
        pass

        break
    else:
        print("Nierozpoznana opcja menu")