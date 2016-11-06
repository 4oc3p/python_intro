import math

# Ввод
input_from = int(input("Проверку начинать с числа: "))
input_to = int(input("Проверку закончить числом: "))


# Ф-я для вывода чисел
def simple_dig(a, b):
    for i in range(a, b):
        if (math.factorial(i - 1) + 1) % i == 0:
            print(i)


simple_dig(input_from, input_to)
