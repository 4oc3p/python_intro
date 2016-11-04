# Ф-я подсчета суммы всех квадратов цифры 3 в промежутке чисел
def sum_of_pow_three(a, b):
    total = 0
    for i in range(a, b+1):
        if i == 1:
            total += 1
        elif i % 3 == 0:
            work = i
            while work % 3 == 0 and i != 0:
                work //= 3
                if work == 1:
                    total += i
    return total

# Вывод результата
print(sum_of_pow_three(0, pow(10, 6)))


# Ф-я подсчета суммы всех квадратов цифры 3 в промежутке чисел №2
def sum_of_pow_three2(a, b):
    total = 0
    power = 0
    for i in range(a, b+1):
        if i == pow(3, power):
            power += 1
            total += i
    return total

# Вывод результата
print(sum_of_pow_three2(0, pow(10, 6)))
