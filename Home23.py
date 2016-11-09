lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def average(l):
    return round(sum(l) / len(l), 2)

print("Среднее арифметическое чисел %s = %s" % (lst, average(lst)))
