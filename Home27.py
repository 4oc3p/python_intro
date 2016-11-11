import random

lst = []


def fill_list(l):
    for i in range(11):
        l += [random.randint(-1, 1)]
    return l


def compare(l):
    minus_zero_one = [0, 0, 0]
    for i in range(0, len(l)):
        if l[i] == -1:
            minus_zero_one[0] += 1
        elif l[i] == 0:
            minus_zero_one[1] += 1
        else:
            minus_zero_one[2] += 1
    # for elem in l:
    #     minus_zero_one[elem + 1] += 1
    return minus_zero_one


def result(l):
    a = compare(l)
    maximum = max(a)
    if a[0] == a[1] or a[1] == a[2] or a[0] == a[2]:
        pass
    elif maximum == a[0]:
        print("В списке больше '-1': %d цифр" % a[0])
    elif maximum == a[1]:
        print("В списке больше '0': %d цифр" % a[1])
    else:
        print("В списке больше '1': %d цифр" % a[2])


print("Заполненный список равен:", fill_list(lst))
result(lst)
