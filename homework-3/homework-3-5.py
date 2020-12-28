def int_func(*args):
    word_list = []
    for words in args:
        word_list.append(words.capitalize())
    return word_list


u_input = input('Введите слово или несколько слов в нижнем регистре через пробел: ').split(' ')
print(' '.join(int_func(*u_input)))
