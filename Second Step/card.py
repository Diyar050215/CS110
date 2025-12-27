import stdio
import stdrandom

rank = stdrandom.uniformInt(2,15)
if rank == 11:
    rankstr= "Jack"
elif rank == 12:
    rankstr= "Queen"
elif rank == 13:
    rankstr= "King"
elif rank == 14:
    rankstr= "Ace"
else:
    rankstr= str(rank)

suit = stdrandom.uniformInt(0,4)
if suit == 0:
    suitstr= "Clubs"
elif suit ==1:
    suitstr= "Diamonds"
elif suit ==2:
    suitstr= "Hearts"
elif suit ==3:
    suitstr= "Spades"

stdio.writeln(rankstr+" "+"of"+" "+suitstr) 