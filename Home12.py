# Ввод данных
number_input = int(input("Введите число для проверки на четность: "))


# Функция
if number_input % 2 == 0:
    print("Число %d четное" % number_input)
elif number_input % 2 != 0:
    print("Число %d нечетное" % number_input)
else:
    print("Error input")
