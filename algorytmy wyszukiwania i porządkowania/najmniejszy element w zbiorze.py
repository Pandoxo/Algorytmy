def MIN(zbior):
    min_num = zbior[0]
    for num in zbior:
        if num < min_num:
            min_num = num

    return min_num
