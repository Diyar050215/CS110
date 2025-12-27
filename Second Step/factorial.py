import stdio
import sys

n = int (sys.argv[1])

result = 1
for i in range ( 1, n+1):
    result = result * i 

stdio.writeln (result)
