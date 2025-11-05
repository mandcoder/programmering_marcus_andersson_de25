import pytest
import math
from circle import Circle
from shape import Shape

# Basic initialization test


def test_circle_initialization():

    c = Circle(0, 0, 5)
    assert c.x == 0
    assert c.y == 0
    assert c.radius == 5


# validation test datatype
def test_invalid_radius_type():
    with pytest.raises(TypeError()):
        Circle(0, 0, "10")  # radius must be int or float


# validation test for negative value
def test_invalid_radius_negative():
    with pytest.raises(ValueError):
        Circle(0, 0, -5)  # radius cannot be a negative value


# validation test for value equal to zero
def test_invalid_radius_zero():

    with pytest.raises(ValueError):
        Circle(0, 0, 0)  # radius must be greater than zero


# property tests
def test_area_property():

    c = Circle(0, 0, 3)
    assert math.isclose(c.area, math.pi * 9)


def test_perimeter_property():
    c = Circle(0, 0, 3)
    assert math.isclose(c.perimeter, 2 * math.pi * 3)


def test_is_unit_circle_true():
    c = Circle(0, 0, 1)
    assert c.is_unit_circle() is True


def test_is_unit_circle_false():
    c = Circle(2, 2, 1)
    assert c.is_unit_circle() is False
