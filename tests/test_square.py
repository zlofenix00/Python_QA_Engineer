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
    assert square.area == area, 'is not correct area'
    assert square.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a',
                         [
                             (-20),
                             (-5.14)
                         ])
def test_square_negative(a):
    with pytest.raises(ValueError):
        Square(a)
