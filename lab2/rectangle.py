from shape import Shape


class Rectangle(Shape):
    """Represents a rectangle with width and height.

    Validates that both are numeric and >= 0.
    Provides properties for area, perimeter,
    and a check if the rectangle is a square.
    """

    def __init__(self, x, y, width, height):
        super().__init__(x, y)

        self.width = width
        self.height = height

    @property
    def width(self):

        return self._width

    @width.setter
    def width(self, value):

        if not isinstance(value, (float, int)):

            raise TypeError(f"width must be int or float, not {type(value)}")

        elif value <= 0:
            raise ValueError(f"width must be greater than zero, not {value}")

        else:
            self._width = value

    @property
    def height(self):

        return self._height

    @height.setter
    def height(self, value):

        if not isinstance(value, (float, int)):

            raise TypeError(f"height must be int or float, not {type(value)}")

        elif value <= 0:
            raise ValueError("height must be greater than zero")

        else:
            self._height = value

    @property
    def area(self):

        return self.height * self.width

    @property
    def perimeter(self):

        return (self.height + self.width) * 2

    def is_square(self):

        if self.width == self.height:
            return True
        else:
            return False
