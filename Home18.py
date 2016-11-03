import random


# Случайное 12-значное число
a = random.randint(1e11, 1e12)


# Преобразование в список
lst_a = [int(i) for i in str(a)]


# Вывод и выбор наибольшей цифры из списка
print(max(lst_a))
