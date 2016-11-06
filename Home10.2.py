# Ввод числа
number_input1 = int(input("Введите 3-х значное число: "))
number_input2 = int(input("Введите любое число: "))

# Функция суммы цифр 3-х значного числа №2
def count2(plus):
    return (plus // 100) + ((plus % 100) // 10) + plus % 10


# Проверка на 3 знака и вывод
if 99 < number_input1 < 1000:
    print("Сумма цифр числа %d равняется %d" % (number_input1, count2(number_input1)))
else:
    print("Число не 3-х значное")


# Ф-я с циклом суммы цифр числа
def sum_of_digits(a):
    total = 0
    while a > 0:
        total += a % 10
        a //= 10
    return total


# Вывод второй ф-ии
print("Сумма цифр числа %d равняется %d" % (number_input2, sum_of_digits(number_input2)))
