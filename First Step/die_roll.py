import stdio
import stdrandom
import sys

n= int(sys.argv[1])

die1= stdrandom.uniformInt(1, n+1)
die2= stdrandom.uniformInt(1,n+1)
sum= die1 + die2

stdio.writeln(str(sum))

