import math
import random

l = [0]*10


def simple_dig(a, b):
    lst = []
    for i in range(a, b):
        if (math.factorial(i - 1) + 1) % i == 0:
            lst += [i]
    return lst


def fill_list(a):
    for i in range(len(a)):
        a[i] = random.choice(simple_dig(1, 100))
    return a

print(fill_list(l))