""" Test cases for the card class """
import unittest

import poker_engine.card as card


class TestCard(unittest.TestCase):
    def test_create_card(self):
        """ Test that we can create a card """
        c = card.Card(card.Suit.HEARTS, card.Rank.ACE)
        self.assertEqual(c.suit, card.Suit.HEARTS)
        self.assertEqual(c.rank, card.Rank.ACE)

    def test_card_equality(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.ACE)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.JACK)
        self.assertEqual(c1, c2)

    def test_king_less_than_ace(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.ACE)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.ACE)
        self.assertLess(c2, c1)

    def test_jack_less_than_king(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.KING)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.JACK)
        self.assertLess(c2, c1)

    def test_ten_less_than_jack(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.JACK)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.TEN)
        self.assertLess(c2, c1)

    def test_nine_less_than_ten(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.TEN)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.NINE)
        self.assertLess(c2, c1)

    def test_eight_less_than_nine(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.NINE)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.EIGHT)
        self.assertLess(c2, c1)

    def test_seven_less_than_eight(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.EIGHT)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.SEVEN)
        self.assertLess(c2, c1)

    def test_six_less_than_seven(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.SEVEN)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.SIX)
        self.assertLess(c2, c1)

    def test_five_less_than_six(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.SIX)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.FIVE)
        self.assertLess(c2, c1)

    def test_four_less_than_five(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.FIVE)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.FOUR)
        self.assertLess(c2, c1)

    def test_three_less_than_four(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.FOUR)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.THREE)
        self.assertLess(c2, c1)

    def test_two_less_than_three(self):
        """ Test that we can compare two cards """
        c1 = card.Card(card.Suit.HEARTS, card.Rank.THREE)
        c2 = card.Card(card.Suit.HEARTS, card.Rank.TWO)
        self.assertLess(c2, c1)


if __name__ == '__main__':
    unittest.main()
