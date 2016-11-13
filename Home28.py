l1 = list(input("Введите строку для шифровки: "))
l2 = ['а', 'б', 'в', 'г', 'д', 'о', '1', '2', '3', '4', '5', '6', '-', '0']


def encrypt(lst1, lst2):
    s = []
    for i in range(0, len(lst1)):
        if lst1[i] in lst2:
            s.append(lst2[(lst2.index(lst1[i]) + 5) % len(lst2)])
        # num = 0
        # while True:
        #     if lst1[i] == lst2[num]:
        #         s += lst2[num + 5]
        #         break
        #     num += 1
    return ''.join(s)


print("Зашифрованная фраза:", encrypt(l1, l2))
