# Ввод данных
number_input = int(input("Введите число для проверки на четность: "))


# Побитовое сравнение
def bit_compare(a):
    return a & 1

if bit_compare(number_input) == 0:
    print("Число %d четное, bit" % number_input)
elif bit_compare(number_input) == 1:
    print("Число %d нечетное, bit" % number_input)
else:
    print("Error input")


# Функция побитового сравнения со строкой
if int(bin(number_input)[-1]) == 0:
    print("Число %d четное, bit_str" % number_input)
elif int(bin(number_input)[-1]) == 1:
    print("Число %d нечетное, bit_str" % number_input)
else:
    print("Error input")


# Функция сравнения по остатку модуля
if number_input % 2 == 0:
    print("Число %d четное" % number_input)
elif number_input % 2 != 0:
    print("Число %d нечетное" % number_input)
else:
    print("Error input")
