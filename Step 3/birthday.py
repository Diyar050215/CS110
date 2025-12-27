import stdarray
import stdio
import stdrandom
import sys

Dpy = 365
trails = (int(sys.argv[1]))
count = 0 # set count to 0 for counting the number start with 0
for t in range(trails):
    birthdaysSeen = stdarray.create1D(Dpy, False)

    while True:   # infinite loop
        count +=1
        birthday = stdrandom.uniformInt(0, Dpy)
        if birthdaysSeen[birthday]: # if the birthday has been seen before will break 
            break
        birthdaysSeen[birthday] = True # mark the birthday as seen 
stdio.writeln(int(count / trails)) # print the average number of people needed to find a birthday match




