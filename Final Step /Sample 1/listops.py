# Returns True if any value in the list a is True, and False otherwise.
def any(a):
    return count(a) > 0
        
# Returns True if all values in the list a are True, and False otherwise.
def all(a):

    return count(a) == len(a)

# Returns True if exactly k values in the list a are True, and False otherwise.
def exactly(a, k):
    return count(a) == k

# Returns the number of True values in the list a.
def count(a):
    total = 0 
    for x in a:
        if x == True:
            total +=1
    return total

# Unit tests the library. [DO NOT EDIT]
def _main():
    import stdio

    a = [False, False, True, False, True, True, True]
    stdio.writeln("a             = " + str(a))
    stdio.writeln("any(a)        = " + str(any(a)))
    stdio.writeln("all(a)        = " + str(all(a)))
    stdio.writeln("exactly(a, 3) = " + str(exactly(a, 3)))
    stdio.writeln("count(a)      = " + str(count(a)))

if __name__ == "__main__":
    _main()
