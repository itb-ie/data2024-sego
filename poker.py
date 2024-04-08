import random


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise Exception(f"Invalid Suit, needs to be one of: {self.SUITS}")
        if rank not in self.RANKS:
            raise Exception(f"Invalid Rank, needs to be one of: {self.RANKS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    # need to be able to print the card!
    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

    def __eq__(self, other):
        return self.RANKS.index(self.rank) == self.RANKS.index(other.rank)


class Deck:
    def __init__(self):
        cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                cards.append(Card(suit=suit, rank=rank))
        cards = tuple(cards)
        self._cards = cards

    def shuffle(self):
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)


class PokerHand:
    def __init__(self, deck):
        hand = []
        for i in range(5):
            hand.append(deck.cards[i])
        self._hand = hand

    @property
    def hand(self):
        return self._hand

    def __str__(self):
        return str(self.hand)

    @property
    def is_flush(self):
        suit = self.hand[0].suit
        for i in range(1, 5):
            if self.hand[i].suit != suit:
                return False
        return True

    @property
    def is_pair(self):
        found = 0
        for i in range(len(self.hand)):
            card = self.hand[i]
            for j in range(i+1, len(self.hand)):
                next_card = self.hand[j]
                if card.rank == next_card.rank:
                    found += 1
        if found == 1:
            return True
        return False

    @property
    def is_pair2(self):
        ranks = []
        pairs_found = 0
        for card in self.hand:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                pairs_found += 1
            if ranks.count(rank) == 3:
                return False
        if pairs_found == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        ranks = []
        pairs_found = 0
        for card in self.hand:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                pairs_found += 1
        if pairs_found == 4:
            return True
        return False

    @property
    def is_set(self):
        ranks = []
        pairs_found = 0
        for card in self.hand:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 3:
                pairs_found += 1
            if ranks.count(rank) == 2:
                return False
        if pairs_found == 3:
            return True
        return False

    @property
    def is_quads(self):
        ranks = []
        pairs_found = 0
        for card in self.hand:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 4:
                pairs_found += 1
        if pairs_found == 4:
            return True
        return False

    @property
    def is_full_house(self):
        ranks = []
        pairs_found = 0
        for card in self.hand:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 3:
                pairs_found += 1
            if ranks.count(rank) == 2:
                pairs_found += 1
        if pairs_found == 5:
            return True
        return False

    @property
    def is_straight(self):
        original_hand = self.hand.copy()
        self.hand.sort()
        distance = Card.RANKS.index(self.hand[-1].rank) - Card.RANKS.index(self.hand[0].rank)
        self._hand = original_hand
        return not self.is_pair and not self.is_2_pair and not self.is_quads and \
            not self.is_set and distance == 4

    @property
    def is_straight_flush(self):
        return self.is_straight and self.is_flush


pairs = 0
while True:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight_flush:
        print(hand)
        pairs += 1
        if pairs == 10:
            break

#
# i = 0
# matches = 0
# while True:
#     i += 1
#     deck = Deck()
#     deck.shuffle()
#     hand = PokerHand(deck)
#     if hand.is_straight:
#         matches += 1
#         # print("Found a flush:")
#         # print(hand)
#         if matches == 100:
#             break
#
# prob = matches / i * 100
# print(f"The probability of a straight house is {prob}%")
