import stdio
import sys

k= int(sys.argv[1])
c= float(sys.argv[2])
epsilon= float(sys.argv[3])

t = c
while abs(1- (c/t**k)) > epsilon:
    t= t- ((t**k)-c) / (k * t ** (k-1))
stdio.writeln(t)
