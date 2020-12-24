string = input('Введите несколько слов через пробел: ').split( )
for word in string:
    n = string.index(word) + 1
    print(str(n) + ' ' + word[:10])
