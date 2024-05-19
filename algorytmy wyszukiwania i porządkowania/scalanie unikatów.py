def scalanie_unikatow(tab1,tab2):
    result = []
    for num in tab1:
        for num2 in result:
            if num == num2:
                break
        else:
            result.append(num)

    for num in tab2:
        for num2 in result:
            if num == num2:
                break
        else:
            result.append(num)


    return result

print(scalanie_unikatow([1,2,2,3,4,4],[5,4,3,2,2,7]))