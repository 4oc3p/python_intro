user_input = int(input("Введите какое количество чисел Фибоначчи требуется просуммировать: "))


def fibonacci_num(n):
    if 0 < n <= 2:
        result = 1
    else:
        result = fibonacci_num(n-1) + fibonacci_num(n-2)
    return result


def fibonacci_sum(a):
    return sum([fibonacci_num(i) for i in range(1, a+1)])


print(fibonacci_sum(user_input))

