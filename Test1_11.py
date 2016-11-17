import Test1_10

list_2d = [[1, 2, 3],
           [5, 6, 7],
           [9, 10, 11]]


def check_even(a):
    l = [x for x in range(len(a[0])) if x % 2 == 0]
    return l


def sort2dlist(a):
    for i in range(len(a)):
        l1 = []
        for j in range(len(a[i])):
            l1.append(a[j][i])


sort2dlist(list_2d)