from markov_model import MarkovModel
import stdio
import sys

# Entry point.
def main():
    # Read k, corrupted message, and text from command line and standard input.
    k = int(sys.argv[1])

    # Read corrupted message from command line
    corrupted = sys.argv[2]
    
    # Read text from standard input
    text = sys.stdin.read()

    # Create Markov model and decode corrupted message.
    model = MarkovModel(text, k)

    # Write decoded message to standard output.
    stdio.writeln(model.replace_unknown(corrupted))

if __name__ == "__main__":
    main()
