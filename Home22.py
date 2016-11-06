import random

first = int(input("Начальное число: "))
last = int(input("Последнее число: "))


def check_digit(a, b):
    rand = random.randint(a, b)
    while True:
        a = int(input("Ваша попытка: "))
        if a == rand:
            print("Угадали! Число действительно", rand)
            break
        elif a < rand:
            print("Неверно! Число больше!")
            continue
        elif a > rand:
            print("Неверно! Число меньше!")
            continue
    print("Поздравляем!")


print("Случайно выбрано число от %d до %d. Попробуйте угадать его!" % (first, last))
check_digit(first, last)