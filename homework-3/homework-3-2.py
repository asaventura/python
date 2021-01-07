def my_func(x, y, z):
    list1 = [x, y, z]
    list1.sort()
    return list1[-1] + list1[-2]


user_input = input('введите три числа через пробел '
                   'и нажмите Enter, чтобы получить '
                   'сумму двух наибольших из них: ').split(' ')
print(my_func(int(user_input[0]), int(user_input[1]), int(user_input[2])))


