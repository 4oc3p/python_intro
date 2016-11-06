import random

# Ввод диапазона чисел.
first = int(input("Начальное число: "))
last = int(input("Последнее число: "))


# Проверка на соответсвие ввода пользователя и рандомного числа
def check_digit(a, b):
    rand = random.randint(a, b)
    while True:
        user_try = int(input("Ваша попытка: "))
        if user_try < a or user_try > b:
            print("Числа только в диапазоне от %d до %d!" % (a, b))
        elif user_try < rand:
            print("Неверно! Число больше!")
            continue
        elif user_try > rand:
            print("Неверно! Число меньше!")
            continue
        else:  # else нормально в этом случае?
            print("Угадали! Число действительно", rand)
            break
    print("Поздравляем!")


print("Случайно выбрано число от %d до %d. Попробуйте угадать его!" % (first, last))
check_digit(first, last)
