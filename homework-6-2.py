class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return str(f'{self.name} {self.surname}')

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


employee = Position("John", "Smith", "engineer", 32000, 5000)
print(employee.get_total_income())
print(employee.get_full_name())
print(employee.position)
