import rsa
import stdio
import sys

# Entry point.
def main():
    n = int(sys.argv[1])  # receive n and d from command line
    d = int(sys.argv[2])

    width = rsa.bitLength(n)  # use rsa.bitLength to determine width
    message = stdio.readAll() # get message from standard input
    
    for i in range(0, len(message) -1 , width):  #for each i in [ 0,len(message-1)] and increments by width]
        s = message[i:i + width]   # get substring of length width
        y = rsa.bin2dec(s) # convert substring to decimal
        decrypted = rsa.decrypt(y, n, d) # decrypt decimal
        stdio.write(chr(decrypted)) # use chr()

if __name__ == "__main__":
    main()
