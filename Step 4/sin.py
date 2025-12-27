import math
import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    x = float(sys.argv[1])
    stdio.writeln(_sin(math.radians(x)))

# Returns sin(x) calculated using the formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def _sin(x):
    total = 0.0 # start with 0
    term = 1.0 # first term is x^1/1!
    sign = 1 # first term is positive
    i = 1 # start with x^1/1!
    while total != total + term: # while adding term changes total
        term = term * (x / i) # compute x^i/i! incrementally
        if i % 2 != 0: # if i is odd
            total += sign * term # add or subtract term
            sign = -sign #toggle sign 
        i += 1 # increment i
    return total 


if __name__ == "__main__":
    main()