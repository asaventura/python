class Road:
    def __init__(self, length, width):
        """
        :param length: длина дороги в метрах
        :param width: ширина дороги в метрах
        """
        self.length = length
        self.width = width

    def asphalt_mass(self, mass, gage):
        """
        :param mass: масса асфальта на 1м^2 дороги толщиной 1см
        :param gage: толщина покрытия асфальтом в сантимертрах
        :return: масса асфальта для покрытия всего дорожного полотна в тоннах
        """
        return self.length * self.width * mass * gage / 1000


west_road = Road(5000, 20)
print(west_road.asphalt_mass(25, 5))
