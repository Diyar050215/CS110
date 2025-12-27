import stdio
import sys
# Converts Celsius as c 
c = float(sys.argv[1])
# write function of Fahrenheit as f
f = 9/5 * c + 32
stdio.writeln( str(c) + "C" + " = " + str(f) + "F")
