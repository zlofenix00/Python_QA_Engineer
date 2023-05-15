from src.circle import Circle
import pytest


@pytest.mark.parametrize('a, area, perimetr',
                         [
                             (10, 314.16, 62.83),
                             (45.14, 6401.37, 283.62)
                         ])
def test_circle_positive(a, area, perimetr):
    circle = Circle(a)
    assert circle.name == 'Circle', 'name is not correct'
    assert circle.area == area, 'is not correct area'
    assert circle.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a',
                         [
                             (-20),
                             (-5.14)
                         ])
def test_circle_negative(a):
    with pytest.raises(ValueError):
        Circle(a)
