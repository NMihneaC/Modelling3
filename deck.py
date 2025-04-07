import random

class Card:
    """
    Class representing a single playing card with a rank and a suit.
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        """
        Initializes a Card instance with a given rank and suit.
        Raises an error if either is invalid.
        :param rank: A string representing the card rank (e.g., "A", "10", "K")
        :param suit: A string representing the card suit (e.g., "♠", "♥")
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Property that returns the card's rank.
        """
        return self._rank

    @property
    def suit(self):
        """
        Property that returns the card's suit.
        """
        return self._suit

    def __str__(self):
        """
        Defines how a card is printed as a string (e.g., "A♠").
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Official string representation of the card. Same as __str__ here.
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Check equality based on rank only (ignores suit).
        :param other: Another Card object
        :return: True if ranks match, False otherwise
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Compare two cards based on rank order.
        :param other: Another Card object
        :return: True if this card is of lower rank than the other
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)


class Deck:
    """
    Class representing a standard 52-card deck.
    """

    def __init__(self):
        """
        Initializes a deck of 52 cards (all combinations of ranks and suits).
        """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """
        Property that returns the list of cards in the deck.
        """
        return self._cards

    def __str__(self):
        """
        Returns the string representation of the entire deck.
        """
        return str(self._cards)

    def shuffle(self):
        """
        Shuffles the deck randomly.
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Deals (removes and returns) the top card from the deck.
        :return: A Card object
        """
        return self.cards.pop(0)

if __name__ == "__main__":
    c1 = Card("A", "♣")
    print(c1.suit, c1.rank)
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)
