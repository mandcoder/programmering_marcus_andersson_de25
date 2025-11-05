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


# Validation tests for width value negative
def test_value_width_negative():
    with pytest.raises(ValueError):
        Rectangle(0, 0, -1, 5)


# Validation tests for width value zero
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


# property tests
def test_area_property():
    rect = Rectangle(0, 0, 10, 5)
    assert rect.area == 50


def test_perimeter_property():
    rect = Rectangle(0, 0, 10, 5)
    assert rect.perimeter == 30


def test_is_square_true():
    rect = Rectangle(0, 0, 7, 7)
    assert rect.is_square() is True


def test_is_square_false():
    rect = Rectangle(0, 0, 10, 5)
    assert rect.is_square() is False


# inheritance test
def test_inherits_from_shape():
    rect = Rectangle(2, 3, 4, 5)
    assert isinstance(rect, Shape)


# translation test
def test_translate_method():
    rect = Rectangle(1, 1, 4, 2)
    rect.translate(3, -1)
    assert rect.x == 4
    assert rect.y == 0


# comparison operators test
def test_comparison_operators():
    r1 = Rectangle(0, 0, 4, 4)  # area = 16
    r2 = Rectangle(0, 0, 4, 4)  # area = 16
    r3 = Rectangle(0, 0, 3, 6)  # area = 18

    # == and !=
    assert r1 == r2
    assert not (r2 == r3)
    assert r1 != r3
    assert r2 != r3
    assert not (r2 != r2)

    # < and >
    assert r1 < r3
    assert not (r1 < r2)
    assert r3 > r1
    assert not (r2 > r3)
    assert not (r2 > r1)

    # <= and >=
    assert r1 <= r2
    assert r1 <= r3
    assert not (r3 <= r1)
    assert not (r3 <= r2)
    assert r3 >= r1
    assert r1 >= r2
    assert not (r2 >= r3)


# REPR / STR test (from shape)
def test_shape_str_and_repr():
    rect = Rectangle(1, 2, 3, 4)
    s = str(rect)
    r = repr(rect)

    # both should include x and y coordinates (from shape)
    assert "x=" in r and "y=" in r
    assert "x=" in s and "y=" in s
