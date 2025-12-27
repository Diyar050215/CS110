import stdio
import sys

n = int ( sys.argv[1])

dragon = "F"
nogard = "F"

for i in range (1, n+1):
    temp = dragon 
    dragon = dragon + "L" + nogard
    nogard = temp + "R" + nogard 

stdio.writeln(dragon)

     