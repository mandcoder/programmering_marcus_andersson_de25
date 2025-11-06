import pytest
from shape import Shape

# when i created this test-file i used ChatGPT


# simple subclass to test comparison logic
class DummyShape(Shape):
    def __init__(self, x, y, area_value):
        super().__init__(x, y)
        self._area = area_value

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._area * 2  # arbitrary dummy formula


# basic initialization and validation tests
def test_shape_initialization_valid():
    s = Shape(2, 3)

    assert s.x == 2
    assert s.y == 3


def test_invalid_x_type():
    with pytest.raises(TypeError):
        Shape("a", 2)


def test_invalid_y_type():
    with pytest.raises(TypeError):
        Shape(2, "b")


# translate test
def test_translate_method():
    s = Shape(1, 1)
    s.translate(3, -2)

    assert s.x == 4
    assert s.y == -1


# REPR and STR tests
def test_shape_repr_and_str():
    s = Shape(1, 2)
    r = repr(s)
    t = str(s)

    assert "x=" in r and "y=" in r
    assert "coordinates" in t
    assert "1" in t and "2" in t


# check_shape test
def test_check_shape_true_for_shape_instance():
    s1 = Shape(0, 0)
    s2 = Shape(1, 1)

    assert s1.check_shape(s2) is True


def test_check_shape_returns_notimplemented_for_non_shape():
    s = Shape(0, 0)
    result = s.check_shape("not_a_shape")

    assert result == NotImplemented


# comparison operator tests
def test_comparison_operators():
    a = DummyShape(0, 0, 10)
    b = DummyShape(0, 0, 10)
    c = DummyShape(0, 0, 20)

    # Reflexivity (object equals itself)
    assert a == a
    assert not (a != a)

    # == and !=
    assert a == b
    assert not (a == c)
    assert a != c

    # < and >
    assert a < c
    assert not (c < a)
    assert c > a
    assert not (a > b)

    # <= and >=
    assert a <= b
    assert a <= c
    assert not (c <= a)
    assert c >= a
    assert b >= a
    assert not (a >= c)
