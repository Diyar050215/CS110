import math
import stdio
import sys

#  recognize the argv[1] as n and read the number from teminal, and the Euclidean distance between the two vectors represented by x and y
n = int(sys.argv[1])
x = []
for i in range(n):
    x.append(stdio.readFloat())
y = []
distance = 0.0
for i in range(n):
    y.append(stdio.readFloat())
    distance += (x[i] - y[i]) ** 2
stdio.writeln ( str(math.sqrt(distance)))