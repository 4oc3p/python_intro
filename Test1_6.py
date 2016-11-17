import math
import random

l = [0]*10


def primes(a, b):
    lst = []
    for i in range(a, b):
        if (math.factorial(i - 1) + 1) % i == 0:
            lst += [i]
    return lst


def fill_list(a):
    primes_list = primes(1, 100)
    for i in range(len(a)):
        a[i] = random.choice(primes_list)
    return a

print(fill_list(l))
