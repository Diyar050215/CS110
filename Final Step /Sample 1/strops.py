# Returns True if the string s starts with the string t, and False otherwise.
def startswith(s, t):
    for i in range(len(t)):
        if s[i] != t[i]:
            return False
    return True

# Returns True if the string s ends with the string t, and False otherwise.
def endswith(s, t):
    for i in range(len(t)):
        if s[-i] != t[-i]:
            return False
    return True
# Returns the number of characters in the string s that are equal to the 
# character c.
def count(s, c):
    total = 0
    for x in s:
        if x == c:
            total += 1
    return total 

        

# Returns a substring of s starting at i (inclusive) and ending at j 
# (inclusive).
def substring(s, i, j):
    a = ""
    for x in range(i, j +1):
        a += s[x]
    return a 


# Unit tests the library. [DO NOT EDIT]
def _main():
    import stdio

    s = "Hello, World"
    stdio.writeln(startswith(s, "Hel"))
    stdio.writeln(startswith(s, "Hey"))
    stdio.writeln(endswith(s, "old"))
    stdio.writeln(endswith(s, "rld"))
    stdio.writeln(count(s, "l"))
    stdio.writeln(substring(s, 7, 11))

if __name__ == "__main__":
    _main()
