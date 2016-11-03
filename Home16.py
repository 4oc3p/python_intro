# Ввод символов пользователем
symb1 = input("Первый символ: ")
symb2 = input("Второй символ: ")


# Ф-я суммы числовых значений символов
def sum_of_symbols(a, b):
    num1, num2 = ord(a), ord(b)  # Перевод символа в число
    total = 0
    while abs(num1 - num2) > 1:  # Проверка, действительно ли пользователь ввел не соседние либо одинаковые символы
        if num1 < num2:
            for i in range(num1, num2+1):
                total += i
        else:
            for i in range(num2, num1+1):
                total += i
        return total
    return 0


# Вывод результата
print("Сумма числовых значений символов %s + %s и всех символов между ними равняется: %d" % (
    symb1, symb2, sum_of_symbols(symb1, symb2)))