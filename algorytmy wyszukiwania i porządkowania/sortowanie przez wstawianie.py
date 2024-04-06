def sortowanie_przez_wstawianie(tab):
    n = len(tab)
    for i in range(1, n):
        pom = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > pom:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = pom
    return tab

print(sortowanie_przez_wstawianie([2,5,3,0,7,1]))