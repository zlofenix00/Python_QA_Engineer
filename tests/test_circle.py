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
    assert circle.get_area() == area, 'is not correct area'
    assert circle.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a',
                         [
                             (-20),
                             (-5.14)
                         ])
def test_circle_negative(a):
    with pytest.raises(ValueError):
        Circle(a)


def test_areas_sum():
    circle_sum = 2296.55
    circle_1 = Circle(10)
    circle_2 = Circle(25.12)
    assert circle_1.add_area(circle_2) == circle_sum


@pytest.mark.parametrize('name', [20, 15])
def test_areas_sum_negative(name):
    circle = Circle(10)
    with pytest.raises(ValueError):
        circle.add_area(name)
