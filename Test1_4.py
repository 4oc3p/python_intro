user_input = int(input("Введите 5-значное число: "))


def result(a):
    r = 1
    for i in range(5):
        if (a % 10) % 2 != 0:
            r *= a % 10
        a //= 10
    return r

print(result(user_input))