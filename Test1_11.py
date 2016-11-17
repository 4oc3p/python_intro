import Test1_10

list_2d = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15],
           [11, 12, 13, 14, 15]]


def check_even(a):
    l = [x for x in range(len(a[0])) if x % 2 == 0]
    return l


def column_even_ascend_odd_descend(a):
    for i in range(len(a[0])):
        l = []
        for j in range(len(a)):
            l.append(a[j][i])
        if i in check_even(a):
            l.sort(reverse=True)
        else:
            l.sort()
        for j in range(len(a)):
            a[j][i] = l[j]
    return a


Test1_10.print_matrix(column_even_ascend_odd_descend(list_2d))