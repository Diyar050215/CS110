import math

class Circle:
    # Constructs a circle of radius r centered at (h, k); when no arguments are given, the circle
    # is a unit circle centered at the origin.
    def __init__(self, h=0, k=0, r=1):
        self._h = h
        self._k = k
        self._r = r

    # Returns the area of this circle.
    def area(self):
        return math.pi * self._r ** 2

    # Returns the circumference of this circle.
    def circumference(self):
        c = 2 * math.pi * self._r
        return c

    # Returns True if this circle contains the point (x, y) and False otherwise.
    def contains(self, x, y):
        d = math.sqrt(((self._h - x) ** 2) + ((self._k -y) ** 2))
        return d <= (self._r) ** 2

    # Returns a new circle whose center is the same as this circle, but with radius r.
    def scale(self, r):
        return Circle(self._h, self._k, r)

    # Returns the Euclidean distance between the centers of this circle and other.
    def distanceTo(self, other):
        d = math.sqrt(((self._h - other._h) ** 2) + ((self._k - other._k) ** 2))
        return (d)

    # Returns True if this circle is the same as other (ie, they have the same centers and radii)
    # and False otherwise.
    def __eq__(self, other):
        return self._h == other._h and self._k == other._k and self._r == other._r
        

    # Returns True if this circle's area is smaller than other's area and False otherwise.
    def __lt__(self, other):
        return self.area() < other.area()

    # Returns a string representation of this circle.
    def __str__(self):
        return "(" + str(self._h) + ", " + str (self._k) + ", "+ str(self._r) + ")"

# Unit tests the data type.
def _main():
    import stdio

    c = Circle()
    d = Circle(1, 1, 2)
    stdio.writeln(c)
    stdio.writeln(d)
    stdio.writeln(c.area())
    stdio.writeln(c.circumference())
    stdio.writeln(c.contains(1, 1))
    stdio.writeln(c.scale(2))
    stdio.writeln(c.distanceTo(d))
    stdio.writeln(c == d or c == c)
    stdio.writeln(d < c)

if __name__ == "__main__":
    _main()
