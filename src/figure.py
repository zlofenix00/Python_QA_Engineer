class Figure:

    def get_area(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.get_area() + figure.get_area(), 2)
        raise ValueError
