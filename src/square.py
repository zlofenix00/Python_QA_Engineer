from src.figure import Figure


class Square(Figure):
    def __init__(self, a: float):
        self.name = 'Square'
        self.__a = a
        self.__raise_value_error(a)

    @staticmethod
    def __raise_value_error(a: float):
        if not (a > 0):
            raise ValueError

    @property
    def area(self) -> float:
        return round(self.__a * self.__a, 2)

    @property
    def perimetr(self) -> float:
        return round(4 * self.__a, 2)

