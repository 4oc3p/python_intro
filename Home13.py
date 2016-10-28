import math

x1 = int(input("1-я окружность X = "))
y1 = int(input("1-я окружность Y = "))
r1 = int(input("1-я окружность R = "))
x2 = int(input("2-я окружность X = "))
y2 = int(input("2-я окружность Y = "))
r2 = int(input("2-я окружность R = "))


# Ф-я расчета пересечения
def length(x_1, y_1, x_2, y_2):
    return round(math.sqrt(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)), 2)


# Ф-я сравнения длины отрезка и суммы радиусов
def cross(r_1, r_2, lng):
    if r_1 + r_2 < lng:
        s = "пересечения нет"
    elif abs(r_1 - r_2) > lng:
        s = "одна окружность внутри другой"
    else:
        s = "пересечение есть"
    return s


print("Результатом вычисления пересечения для окружностей:"
      "\n№1 - с центром x,y(%d,%d) и R = %d"
      "\n№2 - с центром x,y(%d,%d) и R = %d"
      "\nЯвляется: %s" % (x1, y1, r1, x2, y2, r2, cross(r1, r2, length(x1, y1, x2, y2))))
