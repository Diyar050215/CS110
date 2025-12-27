import stdaudio
import stdio
import sys
# Read in the measures from standard input
# Each measure is represented by an integer.
# The first 16 integers, so it will range [0,16]
# the last 16 integers, so it will range [16,32]
measure = stdio.readAllInts()
if len(measure) != 32:
    sys.exit("waltz must contain exactly 32 measures")
for i in range(16):
    if measure[i] < 1 or measure[i] > 176:
        sys.exit("A minuet measure must be from [1, 176]")
for i in range(16,32):
    if measure[i] < 1 or measure[i] > 96:
        sys.exit("A trio measure must be from [1, 96]")
for v in measure[:16]:
    filename = 'data/M' + str(v)
    stdaudio.playFile(filename)
for v in measure[16:]:
    filename = ' data/T' + str(v)
    stdaudio.playFile(filename)


