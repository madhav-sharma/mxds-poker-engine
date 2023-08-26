""" Class for a single card in a deck of cards """
import enum


class Suit(enum.Enum):
    """ Enum for the suit of a card """
    SPADES = "SPADES"
    HEARTS = "HEARTS"
    DIAMONDS = "DIAMONDS"
    CLUBS = "CLUBS"


class Rank(enum.Enum):
    """ Enum for the rank of a card"""
    ACE = 14
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    """Class for a single card in a deck of cards"""
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __str__(self):
        return f"Card: {self.rank.name} of {self.suit.name}"

    def __lt__(self, other):
        return self.rank.value < other.rank.value
