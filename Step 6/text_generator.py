from markov_model import MarkovModel
import stdio
import sys

# Entry point.
def main():
    # Check for correct number of command-line arguments.
    k = int(sys.argv[1])
    n = int(sys.argv[2])

# Read the entire input text from standard input.
    text = sys.stdin.read()

    # Create a Markov model of order k from the input text.
    model = MarkovModel(text, k)
    stdio.writeln(model.gen(text[:k], n))



if __name__ == "__main__":
    main()
