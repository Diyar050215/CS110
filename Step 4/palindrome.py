import stdio
import sys

# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))

# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s): 
    n = len(s)  # set n to length of s
    for i in range( n //2 ): # find the mid of the string
        if s[i] != s[n - i - 1]: # compare characters from start and end
            return False
    return True

if __name__ == "__main__":
    main()
