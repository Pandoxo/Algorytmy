def sortowanie_przez_scalanie(tab1, tab2):
    i1 = 0
    i2 = 0
    result = []
    while len(result) != len(tab1) + len(tab2):
        if i1 == len(tab1):
            result.extend(tab2[i2:])
            break
        elif i2 == len(tab2):
            result.extend(tab1[i1:])
            break

        if tab1[i1] < tab2[i2]:
            result.append(tab1[i1])
            i1 +=1
        elif tab1[i1] == tab2[i2]:
            result.append(tab1[i1])
            result.append(tab2[i1])
            i1 +=1
            i2 +=1
        else:
            result.append(tab2[i2])
            i2 += 1
    return result



print(sortowanie_przez_scalanie([1, 3, 5, 67], [2, 4, 5, 6,8,9]))
