import math
import stdio
import sys
# save the radius from argv[1] to r
# save the height from argv[2] to h
r = float(sys.argv[1])
h = float(sys.argv[2])
# calculate surface area and volume
area = 2 * math.pi * r *( r + h)
stdio.writeln("area" + " = " + str(area))
volume = math.pi * r ** 2 *h
stdio.writeln("volume" + " = " + str(volume))
