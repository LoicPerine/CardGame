from attrs import define

from enums import CardSuits, CardValues

@define
class Card:
    suit: CardSuits
    rank: CardValues

    def __lt__(self, other:'Card'):
        if isinstance(other, Card):
            return self.rank < other.rank
        raise TypeError(f"Cannot compare Card with {type(other)}")  

    def __ge__(self, other:'Card'):
        return not self < other

    def __eq__(self, other:'Card'):
        if isinstance(other, Card):
            return self.rank == other.rank
        raise TypeError(f"Cannot compare Card with {type(other)}")
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"