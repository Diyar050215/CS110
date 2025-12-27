import math
import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    n = int(sys.argv[1])
    x, y = [], []
    for i in range(n):
        x += [stdio.readFloat()]
    for i in range(n):
        y += [stdio.readFloat()]
    stdio.writeln(_distance(x, y))
# Compute and return the Euclidean distance between vectors x and y.
def _distance(x, y):
    n = len(x) # read length of vectors
    d = 0.0 # initialize distance
    for i in range(n): # compute squared differences
       d += ( x[i] - y[i]) ** 2
    return math.sqrt(d) 

if __name__ == "__main__":
    main()
