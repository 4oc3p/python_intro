# Ввод числа
number_input = input("Введите 3-х значное число: ")


# Функция суммы цифр 3-х значного числа
def count(plus):
    return int(plus[0]) + int(plus[1]) + int(plus[2])


# Проверка на 3 знака и вывод
if 99 < int(number_input) < 1000:
    print("Сумма цифр числа %s равняется %s" % (number_input, count(number_input)))
else:
    print("Число не 3-х значное")
