import random
from card import Card
from deck import Deck
from hand import Hand


class Game:
    player_hand: Hand
    dealer_hand: Hand
    deck: Deck
    total_played: int
    player_wins: int
    tie_count: int

    @property
    def playable(self):
        return bool(self.player_hand) and bool(self.dealer_hand)

    def __init__(self):
        self.deck = Deck()
        self.total_played = 0
        self.player_wins = 0
        self.tie_count = 0
        self.__initialize_players_hands()

    def play(self, card_index: int):
        player_card = self.player_hand.pop(card_index)
        dealer_card = self.dealer_hand.pop(random.randint(0, len(self.dealer_hand) - 1))

        if player_card > dealer_card:
            print(f"Player wins with {player_card} against {dealer_card}")
            self.player_wins += self.tie_count + 1
            self.tie_count = 0
        elif player_card < dealer_card:
            print(f"Dealer wins with {dealer_card} against {player_card}")
            self.tie_count = 0
        else:
            print(f"Player and dealer tie with {player_card}")
            self.tie_count += 1

        if self.deck.cards:
            self.player_hand.append(self.deck.draw())
            self.dealer_hand.append(self.deck.draw())
        self.total_played += 1

    def __initialize_players_hands(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        for _ in range(5):
            self.player_hand.append(self.deck.draw())
            self.dealer_hand.append(self.deck.draw())
