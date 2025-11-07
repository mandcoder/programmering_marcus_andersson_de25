class Shape:
    """Base class for 2D shapes with x and y coordinates.

    Validates numeric coordinates.
    Provides translation, abstract area/perimeter,
    and comparison operators based on area.
    """

    def __init__(self, x: float, y: float):

        # initialize coordinates for the shape
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x coordinate must be a number (int or float)")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y coordinate must be a number (int or float)")
        self._y = value

    def translate(self, dx, dy):
        """Translates (moves) the shape by a given offset in the x and y directions.
        This method updates the current position of the shape by adding dx and dy
        to its existing coordinates."""

        self.x += dx
        self.y += dy

    @property
    def area(self) -> None:
        # abstract property (to be implemented in subclasses)
        pass

    @property
    def perimeter(self) -> None:
        # abstract property (to be implemented in subclasses)
        pass

    def __repr__(self):
        return f"Shape x={self.x}, y={self.y}"

    def __str__(self):
        return f"Shape is positioned at coordinates (x={self.x}, y={self.y})"

    # function to check if other is a shape
    def check_shape(self, other):

        if not isinstance(other, Shape):

            return NotImplemented
        else:
            return True

    # six overload operators with comparision based on area
    def __lt__(self, other):

        if self.check_shape(other):

            return self.area < other.area
        else:
            return NotImplemented

    def __le__(self, other):

        if self.check_shape(other):

            return self.area <= other.area

        else:
            return NotImplemented

    def __eq__(self, other):

        if self.check_shape(other):

            return self.area == other.area

        else:
            return NotImplemented

    def __ne__(self, other):

        if self.check_shape(other):

            return self.area != other.area

        else:
            return NotImplemented

    def __gt__(self, other):

        if self.check_shape(other):

            return self.area > other.area

        else:
            return NotImplemented

    def __ge__(self, other):

        if self.check_shape(other):

            return self.area >= other.area
        else:
            return NotImplemented
