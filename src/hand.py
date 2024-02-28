from card import Card

class Hand(list[Card]):

    def __str__(self) -> str:
        return ", ".join(f"({index})"+str(card) for index, card in enumerate(self)) if self else "Empty hand"