import random
from card import Card

class Deck:
    def __init__(self):
        values = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
        suits = ['Hearts','Spades','Diamonds','Clubs']
        self.cards = [Card(v,s) for v in values for s in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        if n == 1:
            return self.cards.pop()
        else:
            drawn = self.cards[-n:]
            self.cards = self.cards[:-n]
            return drawn