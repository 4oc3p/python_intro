l = [-5, 3, 4, 7]


def normalized(a):
    b = 1 / max(abs(x) for x in a)
    return [round(x*b, 3) for x in a]


print(normalized(l))