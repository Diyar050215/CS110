from blob import Blob
from picture import Picture
import stdarray
import stdio
import sys

# A data type to identify blobs in a picture.
class BlobFinder:
    # Constructs a blob finder to find blobs in the picture pic, using a luminance threshold tau.
    def __init__(self, pic, tau):
        self._blobs = []    # List to store identified blobs
        
        self.pic = pic    # Picture in which to find blobs
        self.tau = tau
        
        marked = stdarray.create2D(self.pic.width(), self.pic.height(), False)   # 2D boolean matrix to mark visited pixels
        
        for i in range(self.pic.width()):  # Iterate over each pixel in the picture
            for j in range(self.pic.height()):
                blob = Blob()
                self._findBlob(self.pic, self.tau, i, j, marked, blob)
                if blob.mass() != 0:
                    self._blobs.append(blob)
                

    # Returns a list of all beads (blobs with mass >= pixels).
    def getBeads(self, pixels):   # Filter blobs by mass
        beads = []
        for blob in self._blobs:
            if blob.mass() >= pixels:
                beads.append(blob)
        return beads

    # Identifies a blob using depth-first search. The parameters are the picture (pic), luminance threshold (tau), 
    # pixel column (i), pixel row (j), 2D boolean matrix (marked), and the blob being identified (blob).
    def _findBlob(self, pic, tau, i, j, marked, blob):
        if i >= 640 or j >= 480 or i < 0 or j < 0:  # Check for out-of-bounds
            return
        elif marked[i][j]:
            return
        elif pic.get(i, j).luminance() < tau:
            return
        
        marked[i][j] = True   # Mark the pixel as visited
        
        blob.add(i, j)       # Add pixel to the blob

        # Recursively explore neighboring pixels
        self._findBlob(pic, tau, i + 1, j, marked, blob)
        self._findBlob(pic, tau, i, j + 1, marked, blob)
        self._findBlob(pic, tau, i, j - 1, marked, blob)
        self._findBlob(pic, tau, i - 1, j, marked, blob)
                    
        

# Unit tests the data type [DO NOT EDIT].
def _main():
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = BlobFinder(pic, tau)
    beads = bf.getBeads(pixels)
    stdio.writef("%d Beads:\n", len(beads))
    for blob in beads:
        stdio.writeln(str(blob))
    blobs = bf.getBeads(1)
    stdio.writef("%d Blobs:\n", len(blobs))
    for blob in blobs:
        stdio.writeln(str(blob))

if __name__ == "__main__":
    _main()
