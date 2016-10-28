user_decide = int(input("Введите цифру выбора: "))
user_input1 = input("Первое слово: ")

if user_decide == 1:
    user_name = input("Имя: ")
    print("Hello, %s" % user_name)
elif user_decide == 2:
    a = (len(user_input1) + 1) // 2
    print(user_input1[0:a])
elif user_decide == 3:
    user_input2 = input("Второе слово: ")
    print(user_input1[1:] + user_input2[1:])
elif user_decide == 4:
    print(user_input1[1:-1])
elif user_decide == 5:
    print(user_input1[-2:] * 3)
elif user_decide == 6:
    b = int(input("Кол-во знаков: "))
    c = int(input("Кол-во раз: "))
    print(user_input1[-b:] * c)
elif user_decide == 7:
    a = round(len(user_input1) / 2 + 0.1)
    print(user_input1[:a] + user_input1.upper()[a:])
elif user_decide == 8:
    print(user_input1.upper()[0] + user_input1[1:-1] + user_input1.upper()[-1])
elif user_decide == 9:
    print(user_input1[0::2] + user_input1[1::2])
else:
    print("end")
