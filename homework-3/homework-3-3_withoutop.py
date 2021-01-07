def my_func(x, y):
    """
    принимает целые числа 'x' и 'y'
    возвращает 'x' в степени '-|y|'
    """
    a = int(x)
    b = abs(int(y))
    while b > 1:
        a **= int(x)
        b -= 1
    return 1 / a


u_input = input('Введите через пробел действительное натуральное и '
                'целое отрицательное числа: ').split(' ')
print(my_func(u_input[0], u_input[1]))
