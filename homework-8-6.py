class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        while True:
            try:
                self.a, self.b = float(self.a), float(self.b)
                break
            except ValueError:
                self.a, self.b = input('Введите корректные значения для "а" и "b" через пробел: ').split(' ')

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{( self.a * other.a - self.b * other.b )} + {( self.a * other.b + self.b * other.a )}i'


num_1 = ComplexNum(45.6, 34)
num_2 = ComplexNum(56.4, 45)
print(num_1 + num_2)
print(num_1 * num_2)
