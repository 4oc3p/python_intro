import random

user_input = int(input("Введите количество знаков для генерации пароля: "))


def password(a):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lower = list(alphabet)
    upper = list(alphabet.upper())
    digits = list("1234567890_")
    s = []
    # s = lower + upper + digits
    # random.shuffle(s)
    # return ''.join(s[0:a])
    while len(s) < a:
        if len(s) < a * 0.33:
            s += random.choice(lower)
        elif len(s) < a * 0.66:
            s += random.choice(upper)
        else:
            s += random.choice(digits)
    random.shuffle(s)
    return ''.join(s)


print("Сгенерированный пароль:", password(user_input))
