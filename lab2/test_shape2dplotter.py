"""Unit tests for the Shape2dPlotter class.

These tests verify:
- Shape list initialization and addition.
- Handling of Shape instances and type validation.
- Plot rendering runs without errors.
"""

import pytest
from shape2dplotter import Shape2dPlotter
from shape import Shape
from circle import Circle
from rectangle import Rectangle
import matplotlib.pyplot as plt

# Chatgpt helped me create this test file


# basic initialization tests
def test_plotter_initialization_default():
    plotter = Shape2dPlotter()
    assert isinstance(plotter.shapes, list)
    assert plotter.shapes == []
    assert hasattr(plotter, "fig")
    assert hasattr(plotter, "ax")


def test_plotter_initialization_with_shapes():
    shapes = [Circle(0, 0, 1), Rectangle(1, 1, 2, 3)]
    plotter = Shape2dPlotter(shapes)
    assert plotter.shapes == shapes


# add_shape test
def test_add_valid_shape():
    plotter = Shape2dPlotter()
    circle = Circle(0, 0, 1)
    plotter.add_shapes(circle)
    assert len(plotter.shapes) == 1
    assert isinstance(plotter.shapes[0], Circle)


def test_add_invalid_shape():
    plotter = Shape2dPlotter()
    with pytest.raises(TypeError):
        plotter.add_shapes("not_a_shape")


# draw_all tests
def test_draw_all_runs_without_error(
    monkeypatch,
):  # monkeypatch is temporary replacer to functions during test
    """Ensures draw_all() executes fully without throwing errors."""

    plotter = Shape2dPlotter()
    plotter.add_shapes(Circle(0, 0, 2))
    plotter.add_shapes(Rectangle(1, 1, 2, 3))

    # prevent plt.show() from blocking the test
    monkeypatch.setattr(plt, "show", lambda: None)

    # should run without raising exceptions
    plotter.draw_all()
