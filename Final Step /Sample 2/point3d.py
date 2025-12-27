import math
import stdio


# An immutable data type to represent a point in 3D space.
class Point3D:
    # Constructs a Point3D object given its x, y, and z coordinates.
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    # Returns the distance of this point to the origin.
    def distToOrigin(self):
        p = math.sqrt(self._x ** 2 + self._y ** 2 + self._z ** 2)
        return p

    # Returns the distance of this point to other.
    def distTo(self, other):
        q = math.sqrt(((self._x - other._x) ** 2) + ((self._y - other._y) ** 2) + ((self._z - other._z) ** 2))
        return q
    # Returns a Point3D object whose x, y, and z coordinates are the negative of this point's x, y, and z coordinates.
    def flip(self):
        return Point3D(-self._x, -self._y, -self._z)

    # Returns True if this point's distance to the origin is less than the other point's distance to the origin; and 
    # False otherwise.
    def __lt__(self, other):
        return self.distToOrigin() < other.distToOrigin()

    # Returns True if this point and other have the same distance to the origin; and False otherwise.
    def __eq__(self, other):
        return self.distToOrigin() == other.distToOrigin()

    # Returns a string representation of this point.
    def __str__(self):
        return '(' + str(self._x) + ', ' + str(self._y) + ', ' + str(self._z) +')'


# Unit tests the data type.
def _main():
    p1 = Point3D(1, 0)
    p2 = Point3D(0, 1)
    stdio.writeln(p1)
    stdio.writeln(p2)
    stdio.writeln(p1.distTo(p2))
    stdio.writeln(p1.flip())
    stdio.writeln(p1 < p2)
    stdio.writeln(p1 == p2)

if __name__ == "__main__":
    _main()
