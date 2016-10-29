import math

print("Вид уравнения ax\u00b2 + bx + c = 0")
# Ввод переменных
a, b, c = float(input("Первый коэф. a = ")), float(input("Второй коэф. b = ")), float(input("Свободный член c = "))


# Нахождение дискриминанта
def disc(a, b, c):
    if a > 0:
        return pow(b, 2) - 4 * a * c
    pass


# Вычисление корней
def solution(a, b, d):
    if d > 0:
        x1 = round((-b + math.sqrt(d)) / (2 * a), 4)
        x2 = round((-b - math.sqrt(d)) / (2 * a), 4)
        return x1, x2
    elif d == 0:
        x1 = round(-b / 2 * a, 4)
        return x1
    else:
        pass


print("Решением уравнения, вида %dx\u00b2 + %sx + %s = 0 является: %s" % (a, b, c, solution(a, b, disc(a, b, c))))


