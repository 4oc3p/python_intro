# Ввод данных
numb1 = int(input("Введите число: "))


# Ф-я вычисления факториала через цикл
def fact_of_number(a):
    total = 1
    for i in range(1, a+1):
        total *= i
    return total


# Ф-я вычисления факториала через рекурсию
def fact_recursive(a):
    if a == 0:
        return 1
    else:
        return a * fact_recursive(a - 1)


# Вывод результатов
print("Факториал числа %d:\nМетодом цикла: %d\nМетодом рекурсии: %d" % (
    numb1, fact_of_number(numb1), fact_recursive(numb1)))
