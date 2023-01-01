a = float(input("podaj dlugość boku a:"))
b = float(input("podaj długość boku b:"))
c = float(input("podaj długość boku c:"))

if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
    print("z podanych długości boków można zbudować trójkąt prostokątny")
else:
    print("brak możliwości zbudowania trójkąta prostokątnego")