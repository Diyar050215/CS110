import rsa
import stdio
import sys

# Entry point.
def main():
    lo = int(sys.argv[1])   # Lower bound of prime search interval
    hi = int(sys.argv[2])   # Upper bound of prime search interval
    n, e, d = rsa.keygen(lo, hi)  # Generate RSA keys
    stdio.writeln( str(n) + ' ' + str(e) + ' ' + str(d))

if __name__ == "__main__":
    main()
