# Ввод строк
str1 = input("Введите строку 1: ")
str2 = input("Введите строку 2: ")


# Округление середины до большего
def s_len(a):
    return (len(a) + 1) // 2


# Функция перемещения строк
def move(first, second):
    work = second[0:s_len(str2)] + first + second[s_len(str2):]  # Помещение первой в середину второй
    return first[0:s_len(str1)] + work + first[s_len(str1):]  # Помещение результата в середину первой и возврат


# Вывод
print("Результат совмещения двух строк: %s" % move(str1, str2))
