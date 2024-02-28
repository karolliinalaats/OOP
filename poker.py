"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"

        """
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    def __init__(self):
        """Initialize Hand."""
        self.card_dict = {}
        self.hand = []
        self.suits = ["diamonds", "clubs", "hearts", "spades"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def card_count(self):
        """Put cards in a dictionary."""
        for card in self.hand:
            self.card_dict[card.value] = 0
        for card in self.hand:
            if card.value in self.card_dict:
                self.card_dict[card.value] += 1
            else:
                self.card_dict[card.value] = 1
        a = sorted(self.card_dict.items(), key=lambda i: i[1], reverse=True)
        return a

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        can_add = True
        if len(self.hand) >= 5:
            can_add = False
        for i in range(len(self.hand)):
            if (card.value == self.hand[i].value) and (card.suit == self.hand[i].suit):
                can_add = False
        if card.value not in self.values or card.suit not in self.suits:
            can_add = False
        return can_add

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card) is True:
            self.hand.append(card)
        else:
            pass

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        if card in self.hand:
            return True
        else:
            return False

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card) is True:
            self.hand.remove(card)

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.hand

    def is_straight(self):
        """
        Determine if the hand is a straight.

        A straight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.

        Examples:
        4 5 6 7 8
        K J 10 Q A

        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        card_values = []
        if len(self.card_count()) < 5:
            return False
        else:
            for card in self.card_count():
                if card[0] == "J":
                    card_values.append(11)
                if card[0] == "Q":
                    card_values.append(12)
                if card[0] == "K":
                    card_values.append(13)
                if card[0] == "A":
                    card_values.append(14)
                if card[0] not in "JQKA":
                    card_values.append(int(card[0]))
        sorted_hand_values = sorted(card_values)
        if sorted_hand_values[0] == sorted_hand_values[1] - 1 == sorted_hand_values[2] - 2 == sorted_hand_values[3] - 3 == sorted_hand_values[4] - 4:
            return True
        else:
            return False

    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        for i in range(len(self.hand)):
            if self.hand[i].suit == self.hand[i + 1].suit == self.hand[i + 2].suit == self.hand[i + 3].suit == self.hand[i + 4].suit:
                return True
            else:
                return False

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        if self.is_straight() is True and self.is_flush() is True:
            return True
        else:
            return False

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        temp = []
        for card in self.card_count():
            temp.append(card[1])
        if 2 in temp and 3 in temp:
            return True
        else:
            return False

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        for card in self.card_count():
            if card[1] == 4:
                return True
            else:
                return False

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        for card in self.card_count():
            if card[1] == 3:
                return True
            else:
                return False

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        8 7 6 6 5

        """
        for card in self.card_count():
            if card[1] == 2:
                return True
            else:
                return False

    def get_hand_type(self):
        """
        Return a string representation of the hand.

        Return None (or nothing), if there are less than five cards in hand.

        "straight flush" - Both a straight and a flush
        "flush" - The cards are all of the same suit
        "straight" - The cards can be ordered
        "full_house" - Three cards are of the same value while the other two also share a value.
        "four of a kind" - Four cards are of the same value
        "three of a kind" - Three cards are of the same value
        "pair" - Two cards are of the same value
        "high card" - None of the above

        """
        hand_type = None
        if len(self.hand) < 5:
            hand_type = None
        elif self.is_straight_flush() is True:
            hand_type = "straight flush"
        elif self.is_flush() is True:
            hand_type = "flush"
        elif self.is_straight() is True:
            hand_type = "straight"
        elif self.is_full_house() is True:
            hand_type = "full house"
        elif self.is_four_of_a_kind() is True:
            hand_type = "four of a kind"
        elif self.is_three_of_a_kind() is True:
            hand_type = "three of a kind"
        elif self.is_pair() is True:
            hand_type = "pair"
        else:
            hand_type = "high card"
        return hand_type

    def __repr__(self):
        """
        Return a string representation of the hand.

        I got a {type} with cards: {card list}
        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts

        If a hand type cannot be yet determined, return a list of cards as so:

        I'm holding {cards}
        I'm holding 2 of diamonds, 4 of spades.

        Order of the cards is not important.
        """
        if len(self.hand) < 5:
            return f"I'm holding {self.hand}"
        else:
            return f"I got a {self.get_hand_type()} with cards: {self.hand} "


if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "diamonds"), Card("5", "diamonds"), Card("3", "diamonds"), Card("6", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())
    print(hand)

    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "hearts"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "spades")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("9", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("5", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("3", "spades"), Card("5", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    print(hand.get_hand_type())