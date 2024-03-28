#dla k > 0

def szyrfruj(txt,k):
    result = ""
    k = k % 26
    txt = txt.lower()
    for letter in txt:
        if ord(letter) + k < 123:
            result += chr(ord(letter) +k)
        else:
            result += chr(ord(letter) + k -26)

    return result

def deszyfruj(txt,k):
    k = k % 26
    result = ""
    for letter in txt:
        if ord(letter) - k < 97:
            result += chr(ord(letter) - k + 26)
        else:
            result += chr(ord(letter) - k)

    return  result



