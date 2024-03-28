def dopelnij(txt, k):
    n = len(txt)
    if n % k == 0:
        return txt
    i = 1
    while True:
        if k * i > n:
            dlugosc_dopelnienia = k * i
            break
        i += 1
    return txt + (dlugosc_dopelnienia - n) * "_"


def szyfruj(txt, k):
    txt = dopelnij(txt, k)
    tab = [[] for _ in range(len(txt) // k)]
    result = ""
    index = 0
    for i in range(len(txt) // k):
        for j in range(k):
            tab[i].append(txt[index])
            index += 1
    for i in range(k):
        for j in range(len(txt)//k):
            result += tab[j][i]
    return result

def deszyfruj(txt,k):
    tab = [["" for _ in range(k)] for _ in range(len(txt)//k)]
    index = 0
    result = ""
    for i in range(k):
        for j in range(len(txt)//k):
            tab[j][i] += txt[index]
            index += 1
    for i in range(len(txt)//k):
        for j in range(k):
            result += tab[i][j]

    return result


print(deszyfruj("AMOALAT_AKA_",3))
