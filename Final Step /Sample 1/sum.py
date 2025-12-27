import stdio
import sys
# save the integer from argv[1] to n
n = int(sys.argv[1])
# start counting with 0
sum = 0
# loop from 1 to n
for i in range(1, n+1):
    if i % 2 == 0:
        sum += i ** 2 
stdio.writeln(str(sum))



