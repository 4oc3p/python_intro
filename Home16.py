symb1 = input("Первый символ: ")
symb2 = input("Второй символ: ")


def sum_of_symbols(a, b):
    num1, num2 = ord(a), ord(b)
    total = 0
    while abs(num1 - num2) > 1:
        if num1 < num2:
            for i in range(num1, num2+1):
                total += i
        else:
            for i in range(num2, num1+1):
                total += i
        return total
    return 0

print("Сумма числовых значений символов %s + %s и всех символов между ними равняется: %d" % (
    symb1, symb2, sum_of_symbols(symb1, symb2)))
