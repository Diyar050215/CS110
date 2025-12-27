from blob_finder import BlobFinder
from picture import Picture
import math
import stdio
import sys

# Entry point
def main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    frame = sys.argv[4: ]
    bf = BlobFinder(Picture(frame[0]), tau)
    prevBeads = bf.getBeads(pixels)

    for i in range(1, len(frame)):
        bf = BlobFinder(Picture(frame[i]), tau)
        currBeads = bf.getBeads(pixels)

        for currBead in currBeads:
            closest = math.inf

            for prevBead in prevBeads:
                 d = currBead.distanceTo(prevBead)
                 if d <= delta and d < closest:
                     closest = d

            if closest != math.inf:
                stdio.writef("%.4f\n", closest)
        
        stdio.writeln()
        prevBeads = currBeads

if __name__ == "__main__":
    main()
