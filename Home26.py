import random

lst1 = []
lst2 = []
# lst1 = [0]*5
# lst2 = [0]*5


def fill_list(l):
    for i in range(5):
        l += [random.randint(0, 5)]
        # l[i] = random.randint(0, 5)
    return l


def average(l):
    return round(sum(l) / len(l), 2)


def print_lists(l1, l2):
    print("Первый список: %s, ср.ар. =  %s" % (fill_list(l1), average(l1)))
    print("Второй список: %s, ср.ар. =  %s" % (fill_list(l2), average(l2)))


def results(l1, l2):
    if average(l1) > average(l2):
        print("Среднее арифметическое первого списка больше")
    elif average(l2) > average(l1):
        print("Среднее арифметическое второго списка больше")
    else:
        print("Средние арифметические списков равны")


print_lists(lst1, lst2)
results(lst1, lst2)