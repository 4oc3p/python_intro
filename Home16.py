# Ввод символов пользователем
symb1 = input("Первый символ: ")
symb2 = input("Второй символ: ")


# Ф-я суммы числовых значений символов
def sum_of_symbols(a, b):
    num1, num2 = ord(a), ord(b)  # Перевод символа в число
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    while max_num - min_num > 1:  # Проверка, действительно ли пользователь ввел не соседние либо одинаковые символы
        return sum(range(min_num, max_num + 1))
    return min_num


# Вывод результата
print("Сумма числовых значений символов %s + %s и всех символов между ними равняется: %d" % (
    symb1, symb2, sum_of_symbols(symb1, symb2)))
