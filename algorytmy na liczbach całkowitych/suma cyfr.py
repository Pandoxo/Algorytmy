def suma_cyfr(num):
    result = 0
    while num > 0:
        result += (num % 10) ** 2
        num //= 10
    return result

#juz nie pamiętam o co tu chodziło

def ciekawa_czy_nudna(num):
    tab = [0]*999
    k = 0
    while num != 1:
        tab[k] = num
        num = suma_cyfr(num)
        for i in range(k):
            if tab[i] == num:
                return False
    return True

print(ciekawa_czy_nudna(82))
