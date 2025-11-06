import pytest
import math
from sphere import Sphere


# basic initialization test
def test_sphere_initialization_valid():
    s = Sphere(5)

    assert s.radius == 5


# validation tests
def test_invalid_radius_type():
    with pytest.raises(TypeError):
        Sphere("ten")  # must be int or float


def test_invalid_radius_negative():
    with pytest.raises(ValueError):
        Sphere(-2)


def test_invalid_radius_zero():
    with pytest.raises(ValueError):
        Sphere(0)


# property tests
def test_volume_property():
    s = Sphere(3)
    expected_volume = (4 / 3) * math.pi * 3**3

    assert math.isclose(s.volume, expected_volume)


def test_surface_area_property():
    s = Sphere(3)
    expected_surface_area = 4 * math.pi * 3**2

    assert math.isclose(s.surface_area, expected_surface_area)


def test_circumference_property():
    s = Sphere(3)
    expected_circumference = 2 * math.pi * 3

    assert math.isclose(s.circumference, expected_circumference)


# string represenation tests
def test_sphere_str_contains_values():
    s = Sphere(2)
    text = str(s)

    assert "Sphere with radius" in text
    assert "volume" in text
    assert "2" in text


def test_sphere_repr_matches_str():
    s = Sphere(4)

    assert repr(s) == str(s)
