from symboltable import SymbolTable
import stdio
import stdrandom

class MarkovModel(object):
    # Creates a Markov model of order k from the given text.
    def __init__(self, text, k):

        self._k = int(k)
        self._st = SymbolTable()
        circ_text = text + text[:k]

        for i in range(len(circ_text) - self._k):
            kgram = circ_text[i:i + self._k]
            next_char = circ_text[i + self._k]

            if kgram not in self._st:
                self._st[kgram] = {}

            if next_char in self._st[kgram]:
                self._st[kgram][next_char] += 1
            else:
                self._st[kgram][next_char] = 1



    # Returns the order this Markov model.
    def order(self):
        return self._k  

    # Returns the number of occurrences of kgram in this Markov model; and 0 if kgram is nonexistent. Raises an error 
    # if kgram is not of length k.
    def kgram_freq(self, kgram):

        if len(kgram) != self._k:
            raise ValueError('kgram ' + kgram + ' is not of length ' + str(self._k))
        
        elif kgram not in self._st:
            return 0
        return sum(self._st[kgram].values())

    # Returns number of times character c follows kgram in this Markov model; and 0 if kgram is nonexistent or if it 
    # is not followed by c. Raises an error if kgram is not of length k.
    def char_freq(self, kgram, c):
        if len(kgram) != self._k:
            raise ValueError('kgram ' + kgram + ' is not of length ' + str(self._k))
        
        elif kgram not in self._st:
            return 0
        
        elif c not in self._st[kgram]:
            return 0
        
        return self._st[kgram][c]

    # Returns a random character following kgram in this Markov model. Raises an error if kgram is not of length k or 
    # if kgram is nonexistent.
    def rand(self, kgram):
        if len(kgram) != self._k:
            raise ValueError('kgram ' + kgram + ' is not of length ' + str(self._k))
        
        elif kgram not in self._st:
            raise ValueError('kgram ' + kgram + ' is nonexistent')
        
        index = stdrandom.discrete(list(self._st[kgram].values()))
        a = sorted(list(self._st[kgram].keys()))
        return a[index]

    # Generates and returns a string of length n from this Markov model, the first k characters of which is kgram.
    def gen(self, kgram, n):
        text = kgram

        for i in range(n - self._k):
            text += self.rand(text[i:i + self._k])
        return text


    # Replaces unknown characters (~) in corrupt with most probable characters from this Markov model, and returns 
    # that string.
    def replace_unknown(self, corrupt):
        original = ""
        for i in range(len(corrupt)):
            if corrupt[i] == "~":
                kgram_before = corrupt[i - self._k:i]
                kgram_after = corrupt[i + 1:i + 1 + self._k]
                probs = []
                hypotheses = []
                for h in self._st[kgram_before].keys():
                    hypotheses.append(h)
                    context = kgram_before + h + kgram_after
                    prob = 1.0
                    for i in range(self._k +1):
                        kgram = context[i:i + self._k]
                        c = context[i + self._k]
                        if kgram not in self._st or c not in self._st[kgram]:
                            prob = 0.0
                            break
                        prob *= self.char_freq(kgram, c) / self.kgram_freq(kgram)
                    probs.append(prob)
                best_hypothesis = hypotheses[_argmax(probs)]
                original += best_hypothesis
            else:
                original += corrupt[i]
        return original

# Given a list a, _argmax returns the index of the maximum value in a.
def _argmax(a):
    return a.index(max(a))

# Unit tests the data type [DO NOT EDIT].
def _main():
    model = MarkovModel("gagggagaggcgagaaa", 2)
    stdio.writeln("model       = MarkoveModel(\"gagggagaggcgagaaa\", k = 2)")
    stdio.writef("freq(ag)    = %d\n", model.kgram_freq("ag"))
    stdio.writef("freq(cg)    = %d\n", model.kgram_freq("cg"))
    stdio.writef("freq(gc)    = %d\n", model.kgram_freq("gc"))
    stdio.writef("freq(xx)    = %d\n", model.kgram_freq("xx"))
    stdio.writef("freq(aa, a) = %d\n", model.char_freq("aa", "a"))
    stdio.writef("freq(ga, g) = %d\n", model.char_freq("ga", "g"))
    stdio.writef("freq(gg, c) = %d\n", model.char_freq("gg", "c"))
    stdio.writef("freq(xx, x) = %d\n", model.char_freq("xx", "x"))
    stdio.writef("freq(gg, x) = %d\n", model.char_freq("gg", "x"))

if __name__ == "__main__":
    _main()
