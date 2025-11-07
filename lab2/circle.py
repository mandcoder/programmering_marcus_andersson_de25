from shape import Shape
import math


class Circle(Shape):
    """Represents a circle with center (x, y) and radius.

    Validates that radius is numeric and >= 0.
    Provides properties for area, perimeter,
    and a check if it's a unit circle.
    """

    def __init__(self, x, y, radius):
        super().__init__(x, y)

        self.radius = radius

    @property
    def radius(self):

        return self._radius

    @radius.setter
    def radius(self, value):

        if not isinstance(value, (float, int)):

            raise TypeError(f"radius must be type int or float, not {type(value)}")

        elif value <= 0:
            raise ValueError("Radius must be greater than zero")

        else:
            self._radius = value

    @property
    def area(self):

        return (self.radius**2) * math.pi

    @property
    def perimeter(self):

        return self.radius * 2 * math.pi

    def is_unit_circle(self):

        if self.radius == 1 and self.x == 0 and self.y == 0:
            return True

        else:
            return False
