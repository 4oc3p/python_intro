lst = [1, 2, 3, 42, 51, 65, 74, 83, 92, 102]


def average(l):
    return sum(l) / len(l)

print("Среднее арифметическое чисел %s = %s" % (lst, average(lst)))
