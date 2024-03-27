def fib_rec(n):
    if n < 3:
        return 1
    else:
        return fib_rec(n-2) + fib_rec(n-1)



def fib(n):
    a = 0
    b = 1
    for i in range(n-2):
        b += a
        a = b-a
    return b
print(fib(6))

print(fib_rec(6))