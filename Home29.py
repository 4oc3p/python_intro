import random


def password():
    lower = list("abcdefghijklmnopqrstuvwxyz")
    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = list("1234567890_")
    s = []
    # s = lower + upper + digits
    # random.shuffle(s)
    # return ''.join(s[0:a])
    while len(s) < 8:
        if len(s) < 3:
            s += lower[random.randint(0, len(lower)-1)]
        elif len(s) < 6:
            s += upper[random.randint(0, len(upper)-1)]
        else:
            s += digits[random.randint(0, len(digits)-1)]
    random.shuffle(s)
    return ''.join(s)

print("Сгенерированный пароль:", password())