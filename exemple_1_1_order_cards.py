# example 1-1 An orderly pile of cards
#     1. __getitem__  method
#     2. namedtuple 
#     3. __len__
#     4. sorted(__iterable, key, reversed)
import collections
Card = collections.namedtuple('Card', ['rank', 'suit']) # Jian: create a Class. namedtuple: create a Class without methods.
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)]+list('JQKA') # create the ranks from 2-10 and J Q K A.
    suits = 'spades diamonds clubs hearts'.split()      # create the suits 'spades' 'diamonds' 'clubs' 'hearts'.
    def __init__(self):                                 # initialize the class
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

print("what is Card: ", Card)  # <class '__main__.Card'>

# test
beer_card = Card('7', 'diamonds') # instantiate an object of class Card whose rank is '7' and suit is 'diamonds'.
print("Card: ", beer_card)
print("the rank of beer_card: ", beer_card.rank, "; the suit of beer_card: ", beer_card.suit)

# instantiate an object of class FrenchDeck
deck = FrenchDeck()
print(len(deck))

print(deck[0], deck[-1])   # __getitem__ to make it come true

# python random choice
from random import choice
print("test random choice: ", choice(deck))

# choose the first three cards
print("The first three cards: ", deck[:3])

# choose the 12th card and then take one card every 13:
print("take one card every 13: ", deck[12::13])

# using the __getitem__ method
# for card in deck:
#     print(card)

# for card in reversed(deck):
#     print(card)

suit_values = dict(spades = 3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)