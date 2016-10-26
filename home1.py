import math

# Статические переменные
a = 1
b = 2
c = 3

# input. Альтернатива. Для ввода значения.
"""
a = float(input("Введи число 1: "))
b = float(input("Введи число 2: "))
c = float(input("Введи число 3: "))
"""

# 1
first = round(a + b * (c / 2), 2)
print("Результат №1 для значений a=%.2f, b=%.2f, c=%.2f равен %.2f;" % (a, b, c, first))
first_s = "Результат №1 для значений a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " равен " + str(first) + ";\n"
# 2
a = 4
b = 5
c = 6
second = round((pow(a, 2) + pow(b, 2)) % 2, 2)
print("Результат №2 для значений a=%.2f, b=%.2f, c=%.2f равен %.2f;" % (a, b, c, second))
second_s = "Результат №2 для значений a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " равен " + str(second) + ";\n"
# 3
a = 7
b = 8
c = 9
third = round((a + b) / 12 * c % 4 + b, 2)
print("Результат №3 для значений a=%.2f, b=%.2f, c=%.2f равен %.2f;" % (a, b, c, third))
third_s = "Результат №3 для значений a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " равен " + str(third) + ";\n"
# 4
a = 10
b = 11
c = 12
fourth = round(((a - b * c) / (a + b)) % c, 2)
print("Результат №4 для значений a=%.2f, b=%.2f, c=%.2f равен %.2f;" % (a, b, c, fourth))
fourth_s = "Результат №4 для значений a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " равен " + str(fourth) + ";\n"
# 5
a = 13
b = 14
c = 15
fifth = round(abs(a - b) / pow((a + b), 3) - math.cos(c), 2)
print("Результат №5 для значений a=%.2f, b=%.2f, c=%.2f равен %.2f;" % (a, b, c, fifth))
fifth_s = "Результат №5 для значений a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " равен " + str(fifth) + ";\n"
# 6
a = 16
b = 17
c = 18
sixth = round(math.pow((math.log(1 + c) / -b), 4) + abs(a), 2)
print("Результат №6 для значений a=%.2f, b=%.2f, c=%.2f равен %.2f;" % (a, b, c, sixth))
sixth_s = "Результат №6 для значений a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + " равен " + str(sixth) + ";\n"

# Вывод. В один список только ответы. Не знаю, как нормально вывести по-другому - пришлось искать костыли.
# print("Результаты всех примеров:\n 1 = %.2f;\n 2 = %.2f;\n 3 = %.2f;\n 4 = %.2f;\n 5 = %.2f;\n 6 = %.2f." %
#       (first, second, third, fourth, fifth, sixth))

# Вывод. В один список через строки.
# print(first_s + second_s + third_s + fourth_s + fifth_s + sixth_s)
