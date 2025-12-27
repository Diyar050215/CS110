import stdio
import stdrandom
import sys

# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    primes = _primes(lo,hi)   # Get list of primes in [lo, hi)
    sample = _sample(primes, 2)  # Randomly sample 2 primes from the list
    p, q = sample[0], sample[1] # Unpack the 2 primes
    n = p * q  
    m = (p - 1) * (q - 1)
    a = _primes(2, m)  # Get a list primes from the interval [2, m)
    while True:
        e = _choice(a)  # Randomly choose e from the list
        if m % e != 0:  # Ensure e and m are coprime
            break       # Exit loop if condition is satisfied
    for d in range(1,m):  # Find d such that (e * d) % m == 1
        if (e * d) % m == 1:  #Find a d ∈ [1, m) such that ed mod m = 1
            break
    return (n, e, d)


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    E = (x**e) % n  # Encrypt x using RSA formula
    return E

# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    D = (y ** d) % n  # Decrypt y using RSA formula
    return D

# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2

# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, "0%db" % (width))

# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)

# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    a = []             # Initialize empty list to hold primes
    for p in range(lo, hi):  # Iterate through numbers in [lo, hi)
        if p < 2:    # Skip numbers less than 2
            continue  # Go to next iteration
        isPrime = True  # Assume p is prime
        for i in range( 2, int ( p ** 0.5)+ 1 ):  # Check for factors from 2 to sqrt(p)
            if p % i == 0:   # If p is divisible by i, it's not prime
                isPrime = False  # Set flag to False
                break            # Exit inner loop
        if isPrime:             # If p is prime, add to list
            a += [p]
    return a
    
       
# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    b = []         # Initialize empty list to hold sample
    for i in a:      # Copy all items from a to b
        b += [i]
    stdrandom.shuffle(b)    # Shuffle b randomly
    return b[:k]

# Returns a random item from the list a.
def _choice(a):
    l = len(a)      # Get length of a
    r = stdrandom.uniformInt(0,l - 1)     # Get random index in [0, l-1]
    return a[r]
    
# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))

if __name__ == "__main__":
    _main()
