import math


class Sphere:
    """Class representing a 3D sphere with radius, volume, surface area, and circumference."""

    def __init__(self, radius):

        if not isinstance(radius, (int, float)):

            raise TypeError("radius must be a number greather than zero")

        elif radius <= 0:
            raise ValueError("radius must be a number greater than zero")

        else:
            self.radius = radius

    @property
    def volume(self):

        return (4 / 3) * math.pi * self.radius**3

    @property
    def surface_area(self):

        return 4 * math.pi * self.radius**2

    @property
    def circumference(self):

        return 2 * math.pi * self.radius

    def __str__(self):

        return f"Sphere with radius {self.radius}, volume {self.volume:.2f} and surface area {self.surface_area:.2f}"

    def __repr__(self):

        return f"Sphere with radius {self.radius}, volume {self.volume:.2f} and surface area {self.surface_area:.2f}"
