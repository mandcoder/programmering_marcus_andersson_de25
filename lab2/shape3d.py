class Shape3D:
    """Base class for 3D geometric object"""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


@property
def volume(self):
    # is implemented in subclasses like Cube, Sphere
    pass


@property
def surface_area(self):
    # is implmented in subclasses like Cube, Sphere
    pass
