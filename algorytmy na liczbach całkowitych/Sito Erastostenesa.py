def sito(n):
    tab = [1] * (n + 1)
    tab[1] = 0

    for i in range(2, n // 2):
        if tab[i] == 1:
            for j in range(i * i, n + 1, i):
                tab[j] = 0
    return tab


n = 100
result = sito(n)
for i in range(len(result)):
    if result[i] == 1:
        print(i)
