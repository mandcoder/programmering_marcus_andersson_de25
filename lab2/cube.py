class Cube:
    """Represents a cube with side length a.

    Validates that a >= 0.
    Provides properties for volume and surface area,
    and readable string representations.
    """

    def __init__(self, a):

        if a <= 0:
            raise ValueError("a must be greater than zero")
        else:
            self.a = a

    @property
    def volume(self):

        return self.a**3

    @property
    def surface_area(self):

        return 6 * self.a * self.a

    def __repr__(self):

        return f"Cube(a={self.a})"

    def __str__(self):

        return f"Cube with side length {self.a}"
