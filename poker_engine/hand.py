""" Hand class"""

from card import Card, Rank


class HighCard:
    """
    Class for a high card hand
    """
    def __init__(self, cards: list[Card]):
        if len(cards) == 0:
            raise ValueError("High card hand must have at least one card")
        if len(cards) > 7:
            raise ValueError("High card hand cannot have more than 5 cards")
        self.cards = cards

    def __lt__(self, other):
        if len(self.cards) != len(other.cards):
            raise ValueError("Hands must have the same number of cards")

        self.cards.sort(reverse=True)
        other.cards.sort(reverse=True)

        for i in range(len(self.cards)):
            if self.cards[i] != other.cards[i]:
                return self.cards[i] < other.cards[i]

        return False
