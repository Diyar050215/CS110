import math
import stdio

# Entry point.
def main():
    ETA = 9.135e-4
    RHO = 5e-7
    T = 297
    R=8.31457

    var = 0
    n = 0

    while not stdio.isEmpty():
        d = stdio.readFloat()
        r = d * 0.175e-6
        var += r ** 2
        n += 1
    
    var = var / (2 * n)
    k = 6 * math.pi * var * ETA * RHO / T
    Na = R / k

    stdio.writef('%e\n', Na)

if __name__ == "__main__":
    main()
