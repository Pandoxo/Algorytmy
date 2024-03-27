
def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(n-1):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
        n -= 1

    return l

print(bubble_sort([4,3,2,1,2]))
