import math


# Функция перевода градусов в радианы
def grad2rad(grad):
    return grad * math.pi / 180


# Функция cos(rad)
def cos_rad(rad):
    return math.cos(rad)


# Вывод результата
print("Вычисление cos по градусам:\ncos(60) = %.4f\ncos(45) = %.4f\ncos(40) = %.4f" % (cos_rad(grad2rad(60)), cos_rad(grad2rad(45)), cos_rad(grad2rad(40))))
