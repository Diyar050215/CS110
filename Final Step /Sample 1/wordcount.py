import stdio
import strops
import sys

prefix = str(sys.argv[1])
count = 0
a = stdio.readAllStrings()

for x in a:
    if strops.startswith(x,prefix):
        count += 1

stdio.writeln(count)
