def horner(wspolczynniki, stopien, x):
    if stopien == 0:
        return  wspolczynniki[0]
    return x*horner(wspolczynniki,stopien-1,x) +wspolczynniki[stopien]


