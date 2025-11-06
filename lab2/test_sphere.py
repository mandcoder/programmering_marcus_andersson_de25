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
