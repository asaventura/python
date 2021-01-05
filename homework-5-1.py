with open('test_file.txt') as test_file:
    lines = test_file.readlines()
    print(f'Количество строк в файле — {len(lines)}')
    for line in enumerate(lines):
        print(f'Количество слов в строке {line[0] + 1} — {len(line[1].split(" "))}')
