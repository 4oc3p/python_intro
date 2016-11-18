import random


def mult_table_no_repeats():
    l = []
    for i in range(2, 10):
        for j in range(i, 10):
            l.append("%dx%d" % (i, j))
    return l


def random_choice(a):
    random.shuffle(a)
    return ','.join(a[:15])

print("Случайные 15 примеров:", random_choice(mult_table_no_repeats()))
