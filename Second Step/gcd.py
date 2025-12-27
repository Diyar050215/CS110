import stdio
import sys

p = int(sys.argv[1])
q= int(sys.argv[2])

while p % q != 0:
    r = p % q
    p = q 
    q = r
stdio.writeln(str(q))
    

