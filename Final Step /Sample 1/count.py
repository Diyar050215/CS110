import stdio
import sys
# Read integer n from command line arguments
n = int(sys.argv[1])
# start count with 0
count = 0
# loop from 0 to n and add i to count if i is multiple of 3
for i in range(n + 1):
    if i % 3 == 0:
        count += i
stdio.writeln(count)
