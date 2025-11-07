class Shape3D:
    """Base class for 3D shapes with x, y, z coordinates.

    Validates numeric coordinates.
    Provides abstract volume and surface_area properties,
    and comparison operators based on volume.
    """

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

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

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("z coordinate must be a number (int or float)")
        self._z = value

    @property
    def volume(self):
        # is implemented in subclasses, Cube, Sphere
        pass

    @property
    def surface_area(self):
        # is implemented in subclasses, Cube, Sphere
        pass

    # operator overloads (compare volumes)
    def check_shape3d(self, other):
        if not isinstance(other, Shape3D):
            return NotImplemented
        return True

    def __eq__(self, other):
        if self.check_shape3d(other):
            return self.volume == other.volume

    def __lt__(self, other):
        if self.check_shape3d(other):
            return self.volume < other.volume

    def __le__(self, other):
        if self.check_shape3d(other):
            return self.volume <= other.volume

    def __gt__(self, other):
        if self.check_shape3d(other):
            return self.volume > other.volume

    def __ge__(self, other):
        if self.check_shape3d(other):
            return self.volume >= other.volume

    def __ne__(self, other):
        if self.check_shape3d(other):
            return self.volume != other.volume

    # dunder methoder
    def __repr__(self):
        return f"Shape3D(x={self.x}, y={self.y}, z={self.z})"

    def __str__(self):
        return f"3D shape positioned at (x={self.x}, y={self.y}, z={self.z})"
