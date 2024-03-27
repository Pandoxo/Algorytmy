def anagram(txt1, txt2):
    if len(txt1) != len(txt2):
        return 0
    n = len(txt1)
    licz = [0 for _ in range(127)]

    for i in range(n):
        licz[ord(txt1[i])] += 1
    for j in range(n):
        licz[ord(txt2[j])] -= 1

    for i in range(127):
        if licz[i] != 0:
            return 0
    return 1


print(anagram("zazza","zzzab"))
