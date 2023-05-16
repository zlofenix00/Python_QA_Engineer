from src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.name = 'Triangle'
        self.__a = a
        self.__b = b
        self.__c = c
        self.__raise_value_error(a, b, c)

    @staticmethod
    def __raise_value_error(a: float, b: float, c: float):
        if not (a > 0 and b > 0 and c > 0):
            raise ValueError

    def get_area(self) -> float:
        p = ((self.__a + self.__b + self.__c) / 2)
        return round(math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)), 2)

    @property
    def perimetr(self) -> float:
        return self.__a + self.__b + self.__c
