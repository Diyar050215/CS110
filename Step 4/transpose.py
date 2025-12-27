import stdarray
import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    a = stdarray.create2D(m, n)
    for i in range(m):
        for j in range(n):
            a[i][j] = stdio.readFloat()
    c = _transpose(a)
    for row in c:
        for v in row:
            stdio.write(str(v) + " ")
        stdio.writeln()

# Returns the transpose of a.
def _transpose(a):
    m = len(a) # number of rows
    n = len(a[0]) # number of columns
    c = stdarray.create2D(n,m) # transpose will have n rows and m columns
    for i in range(m): # iterate over rows of a
        for j in range(n): # iterate over columns of a
            c[j][i] = a[i][j] # assign value to transposed position
    return c


if __name__ == "__main__":
    main()
