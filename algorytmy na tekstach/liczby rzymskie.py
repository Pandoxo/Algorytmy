def RomanConv(txt):
    symbols = {'I':1,
               'V':5,
               'X':10,
               'L': 50,
               'C': 100,
               "D": 500,
               "M": 1000}
    result = 0
    for i in range(len(txt) -1):
        if symbols.get(txt[i+1])  > symbols.get(txt[i]):
            result -= symbols.get(txt[i])
        else:
            result += symbols.get(txt[i])
    result += symbols.get(txt[-1])

    return result

def base10Conv(num):

print(RomanConv("CMXCIX"))



