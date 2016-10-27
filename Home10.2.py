# Ввод числа
number_input = int(input("Введите 3-х значное число: "))


# Функция суммы цифр 3-х значного числа №2
def count2(plus):
    return (plus // 100) + ((plus % 100) // 10) + plus % 10


# Проверка на 3 знака и вывод
if 99 < number_input < 1000:
    print("Сумма цифр числа %d равняется %d" % (number_input, count2(number_input)))
else:
    print("Число не 3-х значное")
