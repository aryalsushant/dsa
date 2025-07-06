"""
Step 1: Add the following Hand class to your code that represents a player's hand of cards.

A new instance of Hand is always empty.

Step 2: Add two methods add_card() and remove_card() to the Hand class that each accept a Card object as a parameter.

add_card() should add the Card to the player's Hand
remove_card() should remove the card from the player's Hand.
"""
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, Card):
        self.cards.append(Card)

    def remove_card(self, Card):
        if Card in self.cards:
            self.cards.remove(Card)

#test cases
card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
print(player1_hand.cards)  # []

player1_hand.add_card(card_one)
print(player1_hand.cards)  # [card_one]

player1_hand.add_card(card_two)
print(player1_hand.cards)  # [card_one, card_two]

player1_hand.remove_card(card_one)
print(player1_hand.cards)  # [card_two]

    