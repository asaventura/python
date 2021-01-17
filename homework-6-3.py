class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула {direction}'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}км/ч'


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            return f'Допустимая скорость {self.name} превышена!'
        else:
            return f'Скорость {self.name} - {self.speed}км/ч'


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            return f'Допустимая скорость {self.name} превышена!'
        else:
            return f'Скорость {self.name} - {self.speed}км/ч'


class SportCar(Car):
    def friend_of_walker(self):
        if int(self.speed) > 120:
            return f'Сегодня днем звезда кинофраншизы "Форсаж" Пол Уокер ' \
                   f'разбился на {self.name} своего друга ' \
                   f'на скорости {self.speed}км/ч'


class PoliceCar(Car):
    def __init__(self, speed, name, color, is_police=True):
        Car.__init__(self, speed, name, color)
        self.is_police = is_police


police_car = PoliceCar(100, 'federal markings', 'Pontiac')
print(police_car.is_police)
print(police_car.turn('направо'))
print(police_car.color)
print(police_car.show_speed() + '\n')

sport_car = SportCar(160, 'red', 'Porsche Carrera GT')
print(sport_car.go())
print(sport_car.friend_of_walker() + '\n')

work_car = WorkCar(20, 'yellow', 'погрузчик')
print(work_car.show_speed())
print(work_car.stop() + '\n')

town_car = TownCar(100, 'black', 'Toyota Prius')
print(town_car.show_speed())
print(town_car.turn('в столб'))
