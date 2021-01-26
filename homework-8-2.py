class FloatOnly(Exception):
    def __init__(self, err_txt):
        self.err_txt = err_txt


num_list = []
while True:
    el = input("Введите число, "
               "если хотите завершить формирование списка, "
               "введите 'stop': ")
    if el != 'stop':
        try:
            if el.isdigit():
                num_list.append(el)
            else:
                raise FloatOnly("Вы ввели не число!")
        except FloatOnly as err:
            print(err)
    else:
        break
print(f'Вы ввели следующие числа: {num_list}. Программа завершена.')
