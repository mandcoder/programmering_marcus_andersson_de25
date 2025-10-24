class Shape:

    def __init__(self, x: float, y: float):

        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """Translates (moves) the shape by a given offset in the x and y directions.
        This method updates the current position of the shape by adding dx and dy
        to its existing coordinates."""

        self.x += dx
        self.y += dy

    @property
    def area(self) -> None:

        pass

    @property
    def perimeter(self) -> None:

        pass

    def __repr__(self):

        return f"Shape x={self.x}, y={self.y}"

    def __str__(self):

        return f"Shape is positioned at coordinates (x={self.x}, y={self.y})"

    # overload < operator
    def __lt__(self, other):

        return self.area < other.area

    def __le__(self, other):

        return self.area <= other.area

    def __eq__(self, other):

        return self.area == other.area

    def __ne__(self, other):

        return self.area != other.area

    def __gt__(self, other):

        return self.area > other.area

    def __ge__(self, other):

        return self.area >= other.area
