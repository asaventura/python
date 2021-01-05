with open('test_file.txt', 'a') as new_file:
    while True:
        u_input = input('Введите данные; чтобы завершить создание файла, отправьте пустую строку: ')
        if u_input is str(''):
            break
        else:
            new_file.write(u_input + '\n')
