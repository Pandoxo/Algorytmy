def selection_sort(l):
    n = len(l)

    for i in range(n - 1):
        min_index = i
        j = i + 1
        # petla wyszukująca najmniejszy element
        while j < n:
            if l[j] < l[min_index]:
                min_index = j
            j += 1

        # zamiana elementu najmniejszego w podzbiorze
        # z pierwszą pozycja nieposortowaną
        temp = l[min_index]
        l[min_index] = l[i]
        l[i] = temp

    return l


print(selection_sort([4, 3, 2, 1]))
