user_input1 = float(input("Введите число 1: "))
user_input2 = float(input("Введите число 2: "))


def check2ten(a, b):
    c, d = abs(10 - a), abs(10 - b)
    if c > d:
        return b
    else:
        return a

print("Ближайшее число к 10:", check2ten(user_input1, user_input2))