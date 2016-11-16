user_input1 = float(input("Введите число 1: "))
user_input2 = float(input("Введите число 2: "))


def check2ten(a, b):
    c = abs(10 - a)
    d = abs(10 - b)
    if c > d:
        return user_input2
    else:
        return user_input1

print("Ближайшее число к 10:", check2ten(user_input1, user_input2))