import rsa
import stdio
import sys

# Entry point.
def main():
    n = int(sys.argv[1])  # receive n and e from command line
    e = int(sys.argv[2]) 

    width = rsa.bitLength(n)    # determine width for binary representation
    message = stdio.readAll()   # read entire message from standard input
    
    for c in message:           # for each character in the message
        x = ord(c)              # build decimal representation
        encrypted = rsa.encrypt(x, n, e)  # encrypt the decimal representation
        encryptedBinary = rsa.dec2bin(encrypted, width)  # convert to binary representation
        stdio.write(str(encryptedBinary))     # write encrypted binary to standard output


if __name__ == "__main__":
    main()
