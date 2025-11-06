# jag behöver a som attribut, och som propertries behöver jag volume och ytarea
# 1. variabeln "a" beskriver kubens dimmension
# 2. volume and surface_area beskriver kubens egenskaper
# volume och surface area beräknas automatiskt när de känner till a.
#
class Cube:

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
