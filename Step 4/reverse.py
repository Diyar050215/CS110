import stdio

# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a:
        stdio.writef("%s ", v)
    stdio.writeln()

# Reverses a in place, ie, without creating a new list.
def _reverse(a):
    n = len(a) # read all elements from list a 
    for i in range( n//2 ):  # iterate through half of the list
        temp = a[i] # start exchange the elements 
        a[i] = a[n - i - 1]
        a[n - i - 1] = temp 

if __name__ == "__main__":
    main()
