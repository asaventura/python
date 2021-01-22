class Cell:
    def __init__(self, amount_of_units):
        self.amount_of_units = int(amount_of_units)

    def __str__(self):
        return str(self.amount_of_units)

    def __add__(self, other):
        new_cell = Cell(self.amount_of_units + other.amount_of_units)
        return new_cell

    def __sub__(self, other):
        if abs(self.amount_of_units - other.amount_of_units) > 0:
            new_cell = Cell(abs(self.amount_of_units - other.amount_of_units))
            return new_cell
        else:
            return print('Клетки сожрали друг друга!')

    def __mul__(self, other):
        new_cell = Cell(self.amount_of_units * other.amount_of_units)
        return new_cell

    def __truediv__(self, other):
        """
        перегружается метод деления в целочисленное деление
        """
        if self.amount_of_units >= other.amount_of_units:
            new_cell = Cell(self.amount_of_units // other.amount_of_units)
        else:
            new_cell = Cell(other.amount_of_units // self.amount_of_units)
        return new_cell

    def make_order(self):
        x = self.amount_of_units // 5
        y = self.amount_of_units % 5
        string = '*****\n'
        string *= x
        if y > 0:
            final_string = f'{"*" * y}\n'
            string += final_string
        return print(string)


cell1 = Cell(36)
cell2 = Cell(72)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
cell3 = cell1 / cell2
cell3.make_order()
