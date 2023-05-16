from src.square import Square
import pytest


@pytest.mark.parametrize('a, area, perimetr',
                         [
                             (10, 100, 40),
                             (25.12, 631.01, 100.48)
                         ])
def test_square_positive(a, area, perimetr):
    square = Square(a)
    assert square.name == 'Square', 'name is not correct'
    assert square.get_area() == area, 'is not correct area'
    assert square.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a',
                         [
                             (-20),
                             (-5.14)
                         ])
def test_square_negative(a):
    with pytest.raises(ValueError):
        Square(a)


def test_areas_sum():
    square_sum = 731.01
    square_1 = Square(10)
    square_2 = Square(25.12)
    assert square_1.add_area(square_2) == square_sum


@pytest.mark.parametrize('name', [20, 15])
def test_areas_sum_negative(name):
    square = Square(10)
    with pytest.raises(ValueError):
        square.add_area(name)
