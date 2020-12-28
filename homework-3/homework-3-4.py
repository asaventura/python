def sum_append_func(*args):
    return sum(args)


u_input = input("Введите произвольное количество чисел через пробел: ").split(' ')
sum_list = [int(i) for i in u_input]
append_list = []
while True:
    append_input = input(f'Сумма чисел составила {sum_append_func(*sum_list)}. '
                         f'Введите дополнительные числа для сложения '
                         f'и/или введите "exit", чтобы завершить: ').split(' ')
    if 'exit' in append_input:
        append_input.remove('exit')
        append_list = [int(i) for i in append_input]
        sum_list.extend(append_list)
        print(f'Сумма всех введенных чисел - {sum_append_func(*sum_list)}, '
              f'программа завершена.')
        break
    else:
        append_list = [int(i) for i in append_input]
        sum_list.extend(append_list)
