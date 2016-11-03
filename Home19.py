# Ввод
input_from = int(input("Вывод начинать с числа: "))
input_to = int(input("Вывод закончить числом: "))


# Ф-я для вывода чисел
def from2something(a, b, c=1):
    for i in range(a, b+1, c):
        print(i)


from2something(input_from, input_to)
