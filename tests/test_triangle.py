from src.triangle import Triangle
from src.circle import Circle
import pytest


@pytest.mark.parametrize('a, b, c, area, perimetr',
                         [
                             (20, 15, 30, 133.32, 65),
                             (3, 5, 7, 6.5, 15)
                         ])
def test_triangle_positive(a, b, c, area, perimetr):
    triangle = Triangle(a, b, c)
    assert triangle.name == 'Triangle', 'name is not correct'
    assert triangle.get_area() == area, 'is not correct area'
    assert triangle.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a, b, c',
                         [
                             (-20, 15, 30),
                             (3, -5, 7)
                         ])
def test_triangle_negative(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


def test_areas_sum():
    triangle_sum = 139.82
    triangle_1 = Triangle(20, 15, 30)
    triangle_2 = Triangle(3, 5, 7)
    assert triangle_1.add_area(triangle_2) == triangle_sum


@pytest.mark.parametrize('name', [20, 15])
def test_areas_sum_negative(name):
    triangle = Triangle(20, 15, 30)
    with pytest.raises(ValueError):
        triangle.add_area(name)
