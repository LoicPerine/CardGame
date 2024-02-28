import random
from card import Card
from enums import CardSuits, CardValues

class Deck:
    cards: list[Card]
    
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in CardSuits for rank in CardValues]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop() if self.cards else None