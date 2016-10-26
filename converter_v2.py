# Ввод выбора
user_input = input("Введите c2f для С в F, f2c для F в C: ")


# функция перевода цельсия в фаренгейт
def c2f(c):
    return round(c * 9/5 + 32, 2)


# функция перевода фаренгейта в цельсий
def f2c(f):
    return round((f - 32) * 5/9, 2)


# выбор конверта и подсчет
if user_input == "c2f":
    celsius_input = float(input("Введите градусы цельсия: "))
    print("Фаренгейты: %s" % c2f(celsius_input))
elif user_input == "f2c":
    fahrenheit_input = float(input("Введите градусы фаренгейта: "))
    print("Цельсий: %s" % f2c(fahrenheit_input))
else:
    print("Bad input")
