with open('numbers_rus.txt', 'a') as rus:
    erd = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    # 'erd' is for English-Russian Dictionary
    with open('numbers_eng.txt') as eng:
        for line in eng.readlines():
            rus_line = line.split(' ')
            rus_line[0] = erd.get(rus_line[0])
            rus.write(' '.join(rus_line))
