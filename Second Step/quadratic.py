import math
import stdio
import sys

a = float( sys.argv[1])
b = float( sys.argv[2])
c = float( sys.argv[3])

if  a==0: 
    stdio.writeln("Value of a must not be 0")
else:
    D= (b * b) - (4 * a * c)
   
    if  D < 0: 
        stdio.writeln("Value of discriminant must not be negative")
    else:
            
        root1 = (-b + math.sqrt(D)) / ( 2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a )

        stdio.writeln ( str(root1) + " " + str(root2)) 