def sum_append_func(*args):
    sum_list1 = [int(arg) for arg in args]
    return sum(sum_list1)


with open('num_string.txt', 'a') as num_string:
    num_str = input('Введите несколько чисел через пробел, '
                    'они будут сохранены в файле "num_string.txt": ')
    num_string.write(num_str + '\n')
    nums = num_str.split(' ')
    print(sum_append_func(*nums))
