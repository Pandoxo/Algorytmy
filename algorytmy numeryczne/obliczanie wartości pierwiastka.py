
def pierwiastek(num, e):
    a = 1
    b = num
    while abs(a - b) >e:
        a = (a+b)/2 #srednia arytmetyczna
        b = num/a

    return a



print(pierwiastek(3,0.00000000000001))

