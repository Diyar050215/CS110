import stdio
import sys

n = int(sys.argv[1])
a = 1

while a**3 <= n:
    b= a + 1
    while a**3 + b**3 <=n:
        c = a + 1 
        while c**3 <= n:
            d = c + 1
            while c**3 + d**3 <= n:
                x = a**3 + b**3 
                y= c**3 + d**3
                if x == y:
                    stdio.writeln(str(x) + " = " + str(a) + "^3 + " + str(b) + "^3 = " + str(c) + "^3 + " + str(d) + "^3")
                d += 1 
            c += 1
        b += 1
    a += 1
    

