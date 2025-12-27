from instream import InStream
from symboltable import SymbolTable
import stdio


# Entry point.
def main():
    # Load misspellings from file.
    inStream = InStream("data/misspellings.txt")

    # Read all lines from the input file.
    lines = inStream.readAllLines()

    # Create a symbol table to store misspellings.
    misspellings = SymbolTable()

    # Process each line to populate the symbol table.
    for line in lines:

        # Split the line into tokens (misspelled word and correct spelling).
        tokens = line.split()

        # Store the misspelled word and its correct spelling in the symbol table.
        misspellings[tokens[0]] = tokens[1]

    # Read misspelled words from standard input and output corrections.
    while not stdio.isEmpty():

        # Read a misspelled word from standard input.
        word = stdio.readString()
        
        # Check if the word is in the misspellings symbol table.
        if word in misspellings:
            stdio.writeln(word + ' -> ' + misspellings[word])
        




        





if __name__ == "__main__":
    main()
