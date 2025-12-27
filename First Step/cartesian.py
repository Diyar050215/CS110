import math
import stdio
import sys

r = float(sys.argv[1])
t = float(sys.argv[2])

x = r * (math.cos(t * math.pi / 180))
y = r * (math.sin(t * math.pi / 180))
stdio.writeln(str(x) + " " + str(y))
