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
    return ','.join([random.choice(a) for i in range(15)])


print("Случайные 15 примеров:", random_choice(mult_table_no_repeats()))
