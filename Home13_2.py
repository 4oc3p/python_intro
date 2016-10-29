import math


# Ввод пользователем данных для центра окружности и её радиус
x1, y1, r1 = int(input("1-я окружность X = ")), int(input("1-я окружность Y = ")), abs(float(input("1-я окружность R = ")))
x2, y2, r2 = int(input("2-я окружность X = ")), int(input("2-я окружность Y = ")), abs(float(input("2-я окружность R = ")))


# Ф-я расчета расстояния между центрами окружностей
def length(x_1, y_1, x_2, y_2):
    return round(math.sqrt(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2)), 2)


# Ф-я сравнения длины отрезка и суммы/разницы радиусов окружностей
def is_crossed(r_1, r_2, lng):
    if r_1 + r_2 < lng:
        s = 1
    elif abs(r_1 - r_2) > lng:  # когда одна внутри другой
        if r_1 > r_2:
            s = 2
        else:
            s = 3
    elif r_1 + r_2 == lng:
        s = 4
    else:
        s = 5
    return s


# Вывод результатов
def printer():
    if is_crossed(r1, r2, length(x1, y1, x2, y2)) == 1:
        s = "пересечения нет"
    elif is_crossed(r1, r2, length(x1, y1, x2, y2)) == 2:
        s = "№2 внутри окружности №1"
    elif is_crossed(r1, r2, length(x1, y1, x2, y2)) == 3:
        s = "№1 внутри окружности №2"
    elif is_crossed(r1, r2, length(x1, y1, x2, y2)) == 4:
        s = "окружности соприкасаются"
    else:
        s = "пересечение есть"
    print("Результатом вычисления пересечения окружностей:"
      "\n№1 - с центром x,y(%d,%d) и R = %sсм;"
      "\n№2 - с центром x,y(%d,%d) и R = %sсм;"
      "\nЯвляется: %s" % (x1, y1, r1, x2, y2, r2, s))


printer()
