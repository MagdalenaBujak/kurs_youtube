n = int(input('n = '))

def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    else:
        return 1

print(n, '! =', silnia(n))