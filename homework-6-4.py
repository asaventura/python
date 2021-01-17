class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Надпись чернилами'


class Pencil(Stationery):
    def draw(self):
        return 'Рисунок карандашом'


class Handle(Stationery):
    def draw(self):
        return 'Выделение маркером'


pen = Pen('pen')
print(pen.draw())
pencil = Pencil('pencil')
print(pencil.draw())
handle = Handle('handle')
print(handle.draw())
