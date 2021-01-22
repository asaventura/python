from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def amount_of_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        Clothes.__init__(self, title='Coat')
        self.size = size

    @property
    def amount_of_fabric(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        Clothes.__init__(self, title='Suit')
        self.height = height

    @property
    def amount_of_fabric(self):
        return self.height * 2 + 0.3


coat = Coat(22)
suit = Suit(1.85)
print(coat.amount_of_fabric + suit.amount_of_fabric)
