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
    assert rectangle.area == area, 'is not correct area'
    assert rectangle.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a, b',
                         [
                             (-20, 15),
                             (3, -5)
                         ])
def test_rectangle_negative(a, b):
    with pytest.raises(ValueError):
        Rectangle(a, b)
