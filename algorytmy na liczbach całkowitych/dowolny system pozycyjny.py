# dla systemow od 2 do 16
def zmianaSystemu(num, system):
    result = ""
    while num > 0:
        reszta = num % system
        if reszta > 9:
            result += chr(65 + reszta - 10)
        else:
            result += str(reszta)
        num //= system
    return result[::-1]


print(zmianaSystemu(50, 13))
