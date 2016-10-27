# Ввод строк
string_in1 = input("Введите строку 1: ")
string_in2 = input("Введите строку 2: ")


# Округление середины до большего
def length(str_len):
    return round(len(str_len) / 2 + 0.1)


# Определение середины
l1 = length(string_in1)
l2 = length(string_in2)


# Функция перемещения строк
def move(first, second):
    work = second[0:l2] + first + second[l2:]  # Помещение первой в середину второй
    return first[0:l1] + work + first[l1:]  # Помещение результата в середину первой и возврат результата


# Вывод
print("Результат совмещения двух строк: %s" % move(string_in1, string_in2))
