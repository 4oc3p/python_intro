import math


# Функция перевода градусов в радианы
def grad2rad(grad):
    return math.cos(grad * math.pi / 180)


# Вывод результата
print("Вычисление cos по градусам:\ncos(60) = %.4f\ncos(45) = %.4f\ncos(40) = %.4f" % (
    grad2rad(60), grad2rad(45), grad2rad(40)))
