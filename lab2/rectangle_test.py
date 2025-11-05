import pytest
from rectangle import Rectangle
from shape import Shape


# Basic initialization tests
def test_rectangle_initialization():
    rect = Rectangle(0, 0, 10, 5)
    assert rect.x == 0
    assert rect.y == 0
    assert rect.width == 10
    assert rect.height == 5


# Validation tests for type
def test_invalid_width_type():

    with pytest.raises(TypeError):

        Rectangle(0, 0, "10", 5)


def test_invalid_height_type():

    with pytest.raises(TypeError):

        Rectangle(0, 0, 10, "5")


# Validation tests for width value(negative and zero)
def test_value_width_negative():

    with pytest.raises(ValueError):

        Rectangle(0, 0, -1, 5)


def test_zero_width_value():

    with pytest.raises(ValueError):

        Rectangle(0, 0, 0, 5)


# Validation tests for height value(negative and zero)
def test_invalid_height_value_negative():

    with pytest.raises(ValueError):

        Rectangle(0, 0, 10, -1)


def test_invalid_height_value_zero():

    with pytest.raises(ValueError):

        Rectangle(0, 0, 10, 0)
