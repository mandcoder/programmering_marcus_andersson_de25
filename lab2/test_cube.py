"""Unit tests for the Cube class.

These tests confirm that:
- The Cube initializes with valid side length.
- Volume and surface area are computed correctly.
- Invalid dimensions raise appropriate exceptions.
- String and repr outputs are formatted properly.
"""

import pytest
from cube import Cube


# basic initialization test
def test_cube_initialization_valid():
    c = Cube(5)

    assert c.a == 5


# validation tests
def test_invalid_side_negative():
    with pytest.raises(ValueError):
        Cube(-1)


def test_invalid_side_zero():
    with pytest.raises(ValueError):
        Cube(0)


# property tests
def test_volume_property():
    c = Cube(3)
    expected_volume = 3**3

    assert c.volume == expected_volume


def test_surface_area_property():
    c = Cube(3)
    expected_surface_area = 6 * 3 * 3

    assert c.surface_area == expected_surface_area


# string representation tests
def test_cube_repr():
    c = Cube(4)

    assert repr(c) == "Cube(a=4)"


def test_cube_str():
    c = Cube(4)

    assert str(c) == "Cube with side length 4"
