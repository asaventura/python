def division(x, y):
    if y != 0:
        c = x / y
        print(c)
    else:
        print("Деление на ноль невозможно!")


data = input("Введите делимое и делитель через пробел: ").split(' ')
division(int(data[0]), int(data[1]))
