from src.triangle import Triangle
import pytest


@pytest.mark.parametrize('a, b, c, area, perimetr',
                         [
                             (20, 15, 30, 133.32, 65),
                             (3, 5, 7, 6.5, 15)
                         ])
def test_triangle_positive(a, b, c, area, perimetr):
    triangle = Triangle(a, b, c)
    assert triangle.name == 'Triangle', 'name is not correct'
    assert triangle.area == area, 'is not correct area'
    assert triangle.perimetr == perimetr, 'is not correct perimetr'


@pytest.mark.parametrize('a, b, c',
                         [
                             (-20, 15, 30),
                             (3, -5, 7)
                         ])
def test_triangle_negative(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)
