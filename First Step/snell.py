import math
import stdio
import sys

t1= float(sys.argv[1])
n1= float(sys.argv[2])
n2= float(sys.argv[3])

t2= math.asin ((n1 / n2) * math.sin(t1 * math.pi / 180)) * 180 / math.pi
stdio.writeln(str(t2))
