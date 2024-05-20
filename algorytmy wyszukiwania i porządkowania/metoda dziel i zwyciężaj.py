def binary_search(tab,szukana):
    l = 0
    p = len(tab) -1
    while l<=p:
        sr = (l+p)//2
        if tab[sr] == szukana:
            return sr
        if tab[sr] > szukana:
            p = sr -1
        else:
            l  = sr +1

    return -1


print(binary_search([1,2,3,4,5,6,7,8],6))