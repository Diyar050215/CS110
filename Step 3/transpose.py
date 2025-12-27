import stdarray
import stdio
import sys
# Transpose an m-by-n matrix read from standard input and write the
# transposed n-by-m matrix to standard output.

m = int(sys.argv[1])
n = int(sys.argv[2])

a = stdarray.create2D(m, n, None)
for i in range (m):
    for j in range(n):
        a[i][j] = stdio.readFloat()
c = stdarray.create2D(n, m, None)
for i in range(n):
    for j in range(m):
        c[i][j] = a[j][i]
for i in range(n):
    for j in range(m):
        if j < m - 1:
            stdio.write(str(c[i][j]) + ' ')
        else:
            stdio.writeln(str(c[i][j]))
