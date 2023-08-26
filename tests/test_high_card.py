import unittest

from poker_engine.card import Card, Suit, Rank
from poker_engine.hand import HighCard


def create_high_card_hand(cards: list[Card]):
    """
    Factory function for creating a high card hand
    :param cards:
    :return:
    """
    return HighCard(cards)


class TestHighCard(unittest.TestCase):

    def test_equal_high_card(self):
        """ Test that we can create a high card hand """
        self.assertEqual(
            create_high_card_hand([Card(Suit.HEARTS, Rank.ACE)]),
            create_high_card_hand([Card(Suit.HEARTS, Rank.ACE)])
        )

