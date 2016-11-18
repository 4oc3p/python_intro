import random


def mult_table_no_repeats():
    l = []
    a = 1
    for i in range(2, 10):
        a += 1
        for j in range(a, 10):
                l.append("%dx%d" % (i, j))
    return l


def random_choice(a):
    l = []
    while len(l) < 15:
        b = random.choice(a)
        l.append(b)
        a.remove(b)
    return ','.join(l)

print("Случайные 15 примеров:", random_choice(mult_table_no_repeats()))
