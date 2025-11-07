from shape3d import Shape3D
import math


class Sphere(Shape3D):
    """Represents a 3D sphere with a given radius.

    Validates that radius is numeric and > 0.
    Provides properties for volume, surface area,
    and circumference.
    """

    def __init__(self, x: float, y: float, z: float, radius: float):
        # Anropa basklassens konstruktor för att initiera koordinaterna
        super().__init__(x, y, z)

        # Validera att radius är ett tal
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number (int or float)")

        # Kontrollera att radius är större än noll
        if radius <= 0:
            raise ValueError("radius must be greater than zero")

        # Spara värdet
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
