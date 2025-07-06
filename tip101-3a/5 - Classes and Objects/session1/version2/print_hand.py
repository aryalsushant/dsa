"""
The class Card has been updated below with a new attribute next to represent the card that comes after it in a hand of 
cards.

Write a function print_hand() that accepts a Card object and returns a list of all cards in the hand that come after it.
"""
class Card():
	def  __init__(self, suit, rank, next = None):
		self.suit = suit
		self.rank = rank
		self.next = next
		
def print_hand(starting_card):
	result = []
	current = starting_card
	while current != None:
		result.append(current)
		current = current.next
	return result

#test case
card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print(print_hand(card_one))