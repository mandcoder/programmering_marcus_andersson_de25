import pytest
from shape3d import Shape3D


# dummy class for testing
class DummyShape3D(Shape3D):
    def __init__(self, x, y, z, volume_value):
        super().__init__(x, y, z)
        self._volume = volume_value

    @property
    def volume(self):
        return self._volume

    @property
    def surface_area(self):
        return self._volume * 2


# basic initialization test
def test_shape3d_initialization_valid():
    s = Shape3D(1, 2, 3)
    assert s.x == 1
    assert s.y == 2
    assert s.z == 3


# type validation tests
def test_invalid_x_type():
    with pytest.raises(TypeError):
        Shape3D("a", 2, 3)


def test_invalid_y_type():
    with pytest.raises(TypeError):
        Shape3D(1, "b", 3)


def test_invalid_z_type():
    with pytest.raises(TypeError):
        Shape3D(1, 2, "c")


# repr and str tests
def test_shape3d_repr_and_str():
    s = Shape3D(1, 2, 3)
    r = repr(s)
    t = str(s)
    assert "x=" in r and "y=" in r and "z=" in r
    assert "3D shape" in t
    assert "1" in t and "2" in t and "3" in t


# check shape3d tests
def test_check_shape3d_true_for_shape3d_instance():
    s1 = Shape3D(0, 0, 0)
    s2 = Shape3D(1, 1, 1)
    assert s1.check_shape3d(s2) is True


def test_check_shape3d_notimplemented_for_non_shape3d():
    s = Shape3D(0, 0, 0)
    result = s.check_shape3d("not_3d")
    assert result == NotImplemented


# comparision operators tests
def test_comparison_operators():
    a = DummyShape3D(0, 0, 0, 10)
    b = DummyShape3D(0, 0, 0, 10)
    c = DummyShape3D(0, 0, 0, 20)

    # Reflexivity
    assert a == a
    assert not (a != a)

    # == and !=
    assert a == b
    assert not (a == c)
    assert a != c
    assert not (a != b)

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
