
def czynniki(num):
    result = []
    n = num
    while n > 1:
        for i in range(2,num+1):
            if n % i == 0:
                result.append(i)
                n /= i
                break
    return result

print(czynniki(16))