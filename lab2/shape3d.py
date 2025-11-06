class Shape3D:
    """Base class for 3D geometric object"""

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

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

    # dunder methoder
    def __repr__(self):
        return f"Shape3D(x={self.x}, y={self.y}, z={self.z})"

    def __str__(self):
        return f"3D shape positioned at (x={self.x}, y={self.y}, z= {self.z})"
