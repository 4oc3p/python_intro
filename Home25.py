import random

lst = []


def fill_list(l):
    for i in range(2, 99, 2):
        l += [i]
    return l


def shuffle_list(l):
    random.shuffle(l)
    return l


print("Список, заполненый четными числами от 0 до 99:", fill_list(lst))
print("Перемешанный список из пункта 1: ", shuffle_list(lst))
