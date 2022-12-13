from collections import namedtuple
from itertools import product
from random import shuffle
from typing import List

Card = namedtuple('Card', ('rank', 'suit'))


class Deck:
    card_ranks = []
    card_suits = []

    def __init__(self) -> None:
        self.cards = []
        self.refresh_deck()

    def refresh_deck(self) -> int:
        self.cards = map(Card, product(self.card_ranks, self.card_suits))

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()


class FrenchDeck(Deck):
    card_ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']


class Game:
    def __init__(self, deck: Deck) -> None:
        raise NotImplementedError

    def card_value(self, card: Card) -> int:
        raise NotImplementedError

    def hand_value(self, hand: List[Card]) -> int:
        raise NotImplementedError

    def play(self) -> None:
        raise NotImplementedError