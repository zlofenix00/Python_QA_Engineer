from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize('a, b, area, perimetr',
                         [
                             (10, 15, 150, 50),
                             (25, 40, 1000, 130)
                         ])
def test_rectangle_positive(a, b, area, perimetr):
    rectangle = Rectangle(a, b)
    assert rectangle.name == 'Rectangle', 'name is not correct'
    assert rectangle.get_area() == area, 'is not correct area'
    assert rectangle.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a, b',
                         [
                             (-20, 15),
                             (3, -5)
                         ])
def test_rectangle_negative(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)


def test_areas_sum():
    rectangle_sum = 1150
    rectangle_1 = Rectangle(10, 15)
    rectangle_2 = Rectangle(25, 40)
    assert rectangle_1.add_area(rectangle_2) == rectangle_sum


@pytest.mark.parametrize('name', [20, 15])
def test_areas_sum_negative(name):
    rectangle = Rectangle(10, 15)
    with pytest.raises(ValueError):
        rectangle.add_area(name)
