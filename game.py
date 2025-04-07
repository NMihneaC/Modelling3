from turtle import TurtleScreen
from deck import Deck, Card

class Hand:
    """
    Class representing a poker hand of 5 cards drawn from a deck.
    """

    def __init__(self, deck):
        """
        Initializes the Hand by dealing 5 cards from the provided deck.
        :param deck: An instance of Deck from which to draw cards.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Returns the list of 5 cards in the hand.
        """
        return self._cards

    def __str__(self):
        """
        Returns the string representation of the hand (list of 5 cards).
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Checks if all 5 cards have the same suit (flush).
        :return: True if hand is a flush, else False.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Counts how many times card ranks match among the 5 cards.
        For example:
        - A pair gives 2 matches
        - Two pairs give 4 matches
        - Three of a kind gives 6 matches
        - Full house gives 8 matches
        - Four of a kind gives 12 matches
        :return: Total number of rank matches
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if the hand contains exactly one pair.
        :return: True if one pair, else False
        """
        return self.num_matches == 2

    @property
    def is_2_pair(self):
        """
        Checks if the hand contains exactly two pairs.
        :return: True if two pairs, else False
        """
        return self.num_matches == 4

    @property
    def is_trips(self):
        """
        Checks if the hand contains three of a kind.
        :return: True if three of a kind, else False
        """
        return self.num_matches == 6

    @property
    def is_quads(self):
        """
        Checks if the hand contains four of a kind.
        :return: True if four of a kind, else False
        """
        return self.num_matches == 12

    @property
    def is_fullhouse(self):
        """
        Checks if the hand contains a full house (3 of a kind + a pair).
        :return: True if full house, else False
        """
        return self.num_matches == 8

matches = 0
count = 0

while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    print(hand)
    hand.cards.sort()
    print(hand)
    break
    count += 1
    if hand.is_fullhouse:
        # print(hand)
        matches += 1
        # break

print(f"The probability of a full house is {100*matches/count}%")
