import stdio
import sys

# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))

# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    n = len(s)   # length of s
    if n == 0:   # base case
        return True
    return s[0] == s[n - 1] and _isPalindrome(s[1:n - 1])   # recursive case
    

if __name__ == "__main__":
    main()
