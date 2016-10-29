input_speed1 = int(input("Скорость первого поезда: "))
input_speed2 = int(input("Скорость второго поезда: "))


# Ф-я расчета времени нужного для достижения съезда
def is_crashed(a, b):
    if (4 / a) > (6 / b):
        return True
    else:
        return False


def printer():
    if is_crashed(input_speed1, input_speed2):
        s = "не успеет"
    else:
        s = "успеет"
    print("Два поезда движутся на скорости %d и %d навстречу друг другу. Между ними 10 км. пути.\n"
     "Через 4 км пути первый поезд может свернуть на запасной путь. Он %s." % (input_speed1, input_speed2, s))

printer()
