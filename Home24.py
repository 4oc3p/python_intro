lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def difference(l):
    even, odd = 0, 0
    for i in range(0, len(l)):
        if l[i] % 2 == 0:
            even += l[i]
        else:
            odd += l[i]
    return even - odd


print("Разница сумм четных и нечетных чиссел списка %s равна %s." % (lst, difference(lst)))