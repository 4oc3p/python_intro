l = [4, 2, 14, 4, 5, 16, 17, 85, 9, 10]


def change_dig(a):
    min_ind, max_ind = a.index(min(a)), a.index(max(a))
    a[min_ind], a[max_ind] = a[max_ind], a[min_ind]
    return a


print(change_dig(l))