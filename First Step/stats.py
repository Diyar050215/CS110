import math
import stdio
import stdrandom
import sys

a= int(sys.argv[1])
b= int(sys.argv[2])

x1 = stdrandom.uniformFloat(a,b)
x2 = stdrandom.uniformFloat(a,b)
x3 = stdrandom.uniformFloat(a,b)

m= (x1 + x2 + x3) /3
var= ((x1-m)**2 + (x2-m)**2 + (x3-m)**2) /3
std= math.sqrt(var)
stdio.writeln(str(m) + " " + str(var) + " " + str(std))