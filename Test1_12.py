import random


def mult_table_no_repeats():
    l = []
    for i in range(2, 10):
        for j in range(2, 10):
            if "%dx%d" % (j, i) in l:
                pass
            else:
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
