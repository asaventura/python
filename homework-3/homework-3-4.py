def sum_append_func(*args):
    sum_list1 = [int(arg) for arg in args]
    return sum(sum_list1)


sum_list = input("Введите произвольное количество чисел через пробел: ").split(' ')
while True:
    append_input = input(f'Сумма чисел составила {sum_append_func(*sum_list)}. '
                         f'Введите дополнительные числа для сложения '
                         f'и/или введите "exit", чтобы завершить: ').split(' ')
    if 'exit' in append_input:
        append_input.remove('exit')
        sum_list.extend(append_input)
        print(f'Сумма всех введенных чисел - {sum_append_func(*sum_list)}, '
              f'программа завершена.')
        break
    else:
        sum_list.extend(append_input)
