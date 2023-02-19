
while True:
    try:
        liczba1 = int(input("podaj liczbę: "))
    except:
        print("można podać tylko liczby")
    else:
        break

while True:
    operatory = ["+", "-", "*", "/"]
    znak = input("wybierz znak działania +, -, *, / : ")
    ok = False
    for i in operatory:
        if i == znak:
            ok = True
            break
    if ok == True:
        break

while True:
    try:
        liczba2 = int(input("podaj liczbę: "))
        if liczba2 == 0 and znak == operatory[3]:
            zero = liczba1/liczba2
    except ValueError:
        print("można podać tylko liczby")
    except ZeroDivisionError:
        print("Cholero nie wolno dzielić przez ZERO!")
    else:
        break

if znak == operatory[0]:
    wynik = liczba1 + liczba2
elif znak == operatory[1]:
    wynik = liczba1 - liczba2
elif znak == operatory[2]:
    wynik = liczba1 * liczba2
elif znak == operatory[3]:
    wynik = liczba1 / liczba2


print(f"wynik działania: {wynik}")




