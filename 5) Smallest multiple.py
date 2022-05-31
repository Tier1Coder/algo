for i in range(2520, 99999999999, 2520):
    flag = True
    for divider in range(1, 21):
        if i % divider != 0:
            flag = False
            continue
    if flag == True:
        print(i)
        break
