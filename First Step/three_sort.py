import stdio
import sys

x= int(sys.argv[1])
y= int(sys.argv[2])
z= int(sys.argv[3])

first = min(x,y,z)
last = max(x,y,z)
middle = x + y + z - first - last


stdio.write(str(first)+ " " + str(middle) + " " + str(last))


