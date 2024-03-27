def palindrom(txt):
    n = len(txt)
    for i in range(n//2 + 1):
        if txt[i] != txt[n-1-i]:
            return 0
    return 1
