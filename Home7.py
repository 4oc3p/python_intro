# Ввод даты
input_date = input("Введите дату в американском формате мм.чч.гггг: ")


# Функция смены формата
def change_date(reform):
    return reform[3:6] + reform[0:3] + reform[6:]


# Печать измененного формата
print("В европейском формате это будет: %s" % change_date(input_date))
