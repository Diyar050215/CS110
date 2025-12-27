import stdio
import sys

n = int(sys.argv[1])
count = 0
for i in range(2, n+1):
    j = 2
    while j <= i/j:
        if i % j ==0:
            break
        j+=1
    if j > i/j:
        count +=1
stdio.writeln(count)