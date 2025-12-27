import stdio
import sys

n = int(sys.argv[1])
i = 2

while i <= n/i:
    if n % i == 0:
        break
    i += 1

if i > n/i:
    stdio.writeln("True")
else:
    stdio.writeln("False")

