from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius: float):
        self.name = 'Circle'
        self.__radius = radius
        self.__raise_value_error(radius)

    @staticmethod
    def __raise_value_error(radius: float):
        if not (radius > 0):
            raise ValueError

    @property
    def area(self) -> float:
        return round(math.pi * (self.__radius ** 2), 2)

    @property
    def perimetr(self) -> float:
        return round(2 * math.pi * self.__radius, 2)


circle = Circle(45.14)
print(circle.area)
print(circle.perimetr)

