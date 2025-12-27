from point3d import Point3D
import stdio
import sys

# Entry point.
def main():
    r = float(sys.argv[1]) # Distance threshold from command-line argument

    point = [] # List to store points within distance r from origin

    while not stdio.isEmpty():   # Read until end of input
        x = stdio.readFloat()
        y = stdio.readFloat()
        z = stdio.readFloat()
        p = Point3D(x, y, z)
 
        if p.distToOrigin() <= r:   # Check if point is within distance r
            point.append(p)         # Add p to list point[]

    point.sort()              # Sort points in ascending order of distance to origin

    for p in point:           # Print each point in the sorted list
        stdio.writeln(p)


if __name__ == "__main__":
    main()
