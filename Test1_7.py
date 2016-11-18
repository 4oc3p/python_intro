user_input = int(input("Введите какое количество чисел Фибоначчи требуется просуммировать: "))


# def fibonacci_num(n):
#     if 0 < n <= 2:
#         result = 1
#     else:
#         result = fibonacci_num(n-1) + fibonacci_num(n-2)
#     return result
def fibonacci_num(n):
    l = []
    for i in range(n+1):
        if i == 0:
            l.append(0)
        elif 0 < i <= 2:
            l.append(1)
        else:
            l.append(l[i-1]+l[i-2])
    return l


def fibonacci_sum(a):
    return sum(fibonacci_num(a))


print(fibonacci_sum(user_input))
