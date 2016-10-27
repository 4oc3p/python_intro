import math


# Ввод сторон треугольника
input_width = float(input("Введите ширину треугольника: "))
input_height = float(input("Введите высоту треугольника: "))


# Функция вычисления площади
def square(a, b):
    return round(0.5 * a * b, 2)


# Функция вычисления периметра
def perimeter(a, b):
    c = math.sqrt(pow(a, 2) + pow(b, 2))  # вычисление третьей стороны по теореме Пифагора
    return round(a + b + c, 2)


# Вывод
print("Площадь треугольника со сторонами %s см и %s см равняется %s см, а периметр равен %s см" % (
    input_width, input_height, square(input_width, input_height), perimeter(input_width, input_height)))

