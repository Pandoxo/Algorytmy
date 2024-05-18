def potega(num, n):
    wynik = 1
    while n > 0:
        if n % 2 == 1:
            wynik *= num
        if n == 1:
            return wynik
        num *= num
        n //= 2


print(potega(2, 10))
