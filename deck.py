import numpy as np

class CardDeck:
    def __init__(self, player_count):
        self.player_count = player_count
        self.deck = self.generate_deck()

    def generate_deck(self) -> np.array:
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        values = list(range(14, 1, -1))
        deck = []
        for value in values:
            for suit in suits:
                deck.append((suit, value))


        card_amount = 52 - (52 % self.player_count)
        return np.array(deck[:card_amount])

    def __repr__(self):
        return str(self.deck)

# Example:
deck = CardDeck(3)
print(deck)