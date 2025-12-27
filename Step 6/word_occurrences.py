from instream import InStream
from symboltable import SymbolTable
import stdio
import sys

# Entry point.
def main():
    # Check for correct number of command-line arguments.
    filename = str(sys.argv[1])

    # Load words from the specified file.
    inStream = InStream(filename)

    # Read all words from the input file.
    words = inStream.readAllStrings()

    # Create a symbol table to store word occurrences.
    occurrences = SymbolTable()

    # Process each word to populate the symbol table with their occurrences.
    for i in range(len(words)):
        word = words[i]
        if word not in occurrences:
            occurrences[word] = []
        occurrences[word].append(i)

    # Read words from standard input and output their occurrences.
    while not stdio.isEmpty():
        word = stdio.readString()
        
        # Check if the word is in the occurrences symbol table.
        if word in occurrences:
            stdio.writeln(word + ' -> ' + str(occurrences[word]))
        else:
            stdio.writeln('Word not found')

        


    
if __name__ == "__main__":
    main()
