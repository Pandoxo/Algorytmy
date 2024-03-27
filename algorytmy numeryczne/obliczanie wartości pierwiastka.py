
def pierwiastek(num, e):
    a = 1
    b = num
    while abs(a - b) >e:
        pom = a
        a = (a+b)/2
        b = num/pom

    return a



print(pierwiastek(3,0.00000001))

