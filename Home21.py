start = int(input("Начальное число: "))
end = int(input("Конечное число: "))


def is_1and7_in(a, b):
    for i in range(a, b+1):
        has1, has7 = False, False
        work = i
        while work > 0:
            check_last = work % 10
            work //= 10
            if check_last == 1:
                has1 = True
            if check_last == 7:
                has7 = True
        if has1 == 1 and has7 == 1:
            print(i)

is_1and7_in(start, end)
