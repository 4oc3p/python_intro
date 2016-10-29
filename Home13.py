import math


# Ввод пользователем данных для центра окружности и её радиус
x1, y1, r1 = int(input("1-я окружность X = ")), int(input("1-я окружность Y = ")), abs(float(input("1-я окружность R = ")))
x2, y2, r2 = int(input("2-я окружность X = ")), int(input("2-я окружность Y = ")), abs(float(input("2-я окружность R = ")))


# Ф-я расчета расстояния между центрами окружностей
def length(x_1, y_1, x_2, y_2):
    return round(math.sqrt(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)), 2)


# Ф-я обозначения номеров окружностей
def names(r_first, r_second):
    if r_first > r_second:
        s = "№2 внутри окружности №1"
    else:
        s = "№1 внутри окружности №2"
    return s


# Ф-я сравнения длины отрезка и суммы/разницы радиусов окружностей
def cross(r_1, r_2, lng):
    if r_1 + r_2 < lng:
        s = "пересечения нет"
    elif abs(r_1 - r_2) > lng:  # когда одна внутри другой
        s = names(r_1, r_2)
        """  как более правильно?
        if r_1 > r_2:
            s = "№2 внутри окружности №1"
        else:
            s = "№1 внутри окружности №2"
        """
    elif r_1 + r_2 == lng:
        s = "окружности соприкасаются"
    else:
        s = "пересечение есть"
    return s


# Вывод результатов
print("Результатом вычисления пересечения окружностей:"
      "\n№1 - с центром x,y(%d,%d) и R = %sсм;"
      "\n№2 - с центром x,y(%d,%d) и R = %sсм;"
      "\nЯвляется: %s" % (x1, y1, r1, x2, y2, r2, cross(r1, r2, length(x1, y1, x2, y2))))
