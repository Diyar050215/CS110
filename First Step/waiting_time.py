import math
import stdio
import sys

l = float(sys.argv[1])
t = float(sys.argv[2])

p= math.exp(-l * t)

stdio.writeln(str(p))
