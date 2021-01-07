def my_func(x, y):
    return int(x) ** int(y)


u_input = input('Введите через пробел действительное натуральное и '
                'целое отрицательное числа: ').split(' ')
print(my_func(u_input[0], u_input[1]))
