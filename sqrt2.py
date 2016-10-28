# Ввод числа
user_input = int(input("Введите число для проверки на четность: "))


# Функция проверки числа
def check(a):
    return a > 0 and (a & (~a + 1) == a)  # побитовое сравнение чисел


# Условие вывода
if check(user_input):
    print("Число четное")
else:
    print("Число нечетное")
