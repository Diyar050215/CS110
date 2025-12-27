import listops
import stdio
# read booleans from standard input into a list
a = [] 
while not stdio.isEmpty(): 
    a += [stdio.readBool()]
# the length of the list a - the count of True values in a
stdio.writeln(len(a) - listops.count(a))



