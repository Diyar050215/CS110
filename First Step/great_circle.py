import math
import stdio
import sys

x1=float(sys.argv[1])
y1=float(sys.argv[2])
x2=float(sys.argv[3])
y2=float(sys.argv[4])

r0 = math.pi / 180
d= 6359.83 * math.acos(math.sin(x1 * r0 ) * math.sin(x2 * r0) + math.cos(x1 * r0) * math.cos(x2 * r0) * math.cos((y1-y2) * r0)) 
stdio.writeln(str(d))