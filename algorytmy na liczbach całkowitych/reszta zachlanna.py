def reszta(num,monety):
    iloscMonet = len(monety)
    reszta = 0
    uzyteMonety = []
    while num > 0:
        for i in range(iloscMonet-1,-1,-1):
            if monety[i] < num +1:
                uzyteMonety.append(monety[i])
                num -= monety[i]
                break
    return uzyteMonety

print(reszta(21,[1,2,5]))




