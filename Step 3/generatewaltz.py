import stdarray
import stdrandom
import stdio
# Read in the two-dimensional arrays for the minuet and trio measures
# and romdomly generate a waltz by selecting measures from each.
# Each measure is represented by an integer.
minuetMeasures = stdarray.create2D(11, 16,0)
for i in range (11):
    for j in range(16):
        minuetMeasures[i][j] = stdio.readInt()
trioMeasures = stdarray.create2D(6,16,0)
for i in range(6):
    for j in range(16):
        trioMeasures[i][j] = stdio.readInt()

for j in range(16):
    i = stdrandom.uniformInt(1,6) + stdrandom.uniformInt(1,6)
    stdio.write(str(minuetMeasures[i-2][j]) + ' ')
for j in range(16):
    i = stdrandom.uniformInt(1,7)
    stdio.write(str(trioMeasures[i-1][j]) + ' ')
stdio.writeln()

