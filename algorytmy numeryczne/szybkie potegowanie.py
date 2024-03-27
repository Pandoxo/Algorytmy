def potega(num, n):
    wynik = 1
    while n > 0:
        if n % 2 == 1:
            wynik *= num
        num *= num
        n //= 2
    return wynik
print(potega(2,10))