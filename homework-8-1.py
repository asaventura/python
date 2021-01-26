class MyZeroDivisionError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise MyZeroDivisionError('Деление на ноль невозможно!')
except MyZeroDivisionError as err:
    print(err)
else:
    print(a / b)
finally:
    print('Программа завершена')
