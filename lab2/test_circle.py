"""Unit tests for the Circle class.

These tests verify that:
- Radius validation is enforced.
- Area and circumference calculations are correct.
- Translation and string representation work as expected.
"""

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
    with pytest.raises(TypeError):
        Circle(0, 0, "10")


# validation test for negative value
def test_invalid_radius_negative():
    with pytest.raises(ValueError):
        Circle(0, 0, -5)


# validation test for value equal to zero
def test_invalid_radius_zero():
    with pytest.raises(ValueError):
        Circle(0, 0, 0)


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


# inheritanse tests
def test_inherits_from_shape():
    c = Circle(1, 2, 3)
    assert isinstance(c, Shape)


# translation test
def test_translate_method():
    c = Circle(1, 1, 2)
    c.translate(3, -1)
    assert c.x == 4
    assert c.y == 0


# comparison operators test
# i have used chatgpt to cover all test cases
def test_comparison_operators():
    c1 = Circle(0, 0, 2)  # area = 4π
    c2 = Circle(0, 0, 2)  # area = 4π
    c3 = Circle(0, 0, 3)  # area = 9π

    # == and !=
    assert c1 == c2
    assert not (c2 == c3)
    assert c1 != c3
    assert c2 != c3
    assert not (c2 != c2)

    # < and > (both True/False)
    assert c1 < c3
    assert not (c1 < c2)
    assert c3 > c1
    assert not (c2 > c3)
    assert not (c2 > c1)

    # <= and >= (both True False)
    assert c1 <= c2
    assert c1 <= c3
    assert not (c3 <= c1)
    assert not (c3 <= c2)
    assert c3 >= c1
    assert c1 >= c2
    assert not (c2 >= c3)


# REPR / STR tests from (shape)
def test_shape_str_and_repr():
    c = Circle(1, 2, 3)
    s = str(c)
    r = repr(c)

    # Both should include x and y coordinates (from shape)
    assert "x=" in r and "y=" in r
    assert "x=" in s and "y=" in s
