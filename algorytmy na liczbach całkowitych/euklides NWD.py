def nwd(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % b

    return a


def nwd_rec(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)
print(nwd_rec(100,50))