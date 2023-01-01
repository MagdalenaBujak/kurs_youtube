print("podaj trzy liczby:")

a = int(input("podaj liczbę a:"))
b = int(input("podaj liczbę b:"))
c = int(input("podaj liczbę c:"))

if a >b and a > c and b > c:
    print(f"{c},{b},{a}")
elif a > b and a > c and c > b:
    print(f"{b},{c},{a}")
elif b > a and b > c and a > c:
    print(f"{c},{a},{b}")
elif b > a and b > c  and c > a:
    print(f"{a},{c},{b}")
elif c > a and c > b and a > b:
    print(f"{b},{a},{c}")
elif c > a and c > b and b > a:
    print(f"{a},{b},{c}")



