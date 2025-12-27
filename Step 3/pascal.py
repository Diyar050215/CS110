import stdarray
import stdio
import sys
# Generate Pascal's triangle with n rows read from command line
# and write it to standard output.

n= int(sys.argv[1])
a = stdarray.create1D(n+1, None)
for i in range(n+1):
    a[i] = stdarray.create1D(i+1, 1)
for i in range(n+1):
    for j in range(1,i):
        a[i][j] = a[i-1][j-1] + a[i-1][j]
for i in range(n+1):
    for j in range(i+1):
        if j < i:
            stdio.write((str(a[i][j]) + ' '))
        else:
            stdio.writeln(str(a[i][j]))