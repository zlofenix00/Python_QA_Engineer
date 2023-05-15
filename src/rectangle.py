from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.name = 'Rectangle'
        self.__a = a
        self.__b = b
        self.__raise_value_error(a, b)

    @staticmethod
    def __raise_value_error(a: float, b: float):
        if not (a > 0 and b > 0):
            raise ValueError

    @property
    def area(self) -> float:
        return self.__a * self.__b

    @property
    def perimetr(self) -> float:
        return (self.__a + self.__b) * 2



