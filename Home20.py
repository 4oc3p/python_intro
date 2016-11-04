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


print(sum_of_pow_three(0, 1000000))