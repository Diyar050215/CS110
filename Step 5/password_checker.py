import stdio
import sys

# Entry point [DO NOT EDIT].
def main():
    pwd = sys.argv[1]
    stdio.writeln(_isValid(pwd))

# Returns True if pwd is a valid password, and False otherwise.
def _isValid(pwd):
    if len(pwd) < 8: # Minimum length requirement
        return False
    
    has_upper = False  # Flags for character types
    has_lower = False
    has_digit = False
    has_special = False

    for i in pwd:       # Check each character
        if i.isupper():  
            has_upper = True
        elif i.islower():    
            has_lower = True
        elif i.isdigit():
            has_digit = True
        elif not i.isalnum():
            has_special = True

    return has_upper and has_lower and has_digit and has_special  # Final validation

    
    
    
if __name__ == "__main__":
    main()
