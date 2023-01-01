print("podaj trzy różne liczby:")

a = int(input("podaj wartość dla liczby a:"))
b = int(input("podaj wartość dla liczby b:"))
c = int(input("podaj wartość dla liczby c:"))

if a > b and a > c:
    print(f"liczba {a} jest większa od liczby {b} i {c}")
elif b > a and b > c:
    print(f"liczba {b} jest większa od liczby {a} i {c}")
elif c > a and c > b:
    print(f"liczba {c} jest większa {a} i od liczby {b}")
