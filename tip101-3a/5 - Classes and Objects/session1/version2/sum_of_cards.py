"""
Write a function sum_hand() that takes in an instance of Hand as a parameter and returns the summed value of all 
cards in the hand.

Use the methods from Problems 5-7 to assist you.
If any card in the hand is invalid, return None.
"""
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.is_valid = True
		self.validity()
		
	def validity(self):
		suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		
		if self.suit in suits and self.rank in ranks:
			self.is_valid = True
		else:
			self.is_valid = False
		#solution here
	
		
	def get_value(self):
		if self.is_valid == False:
			return None
		else:
			if self.rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
				return int(self.rank)
			elif self.rank == "Ace":
				return 1
			elif self.rank == "Jack":
				return 11
			elif self.rank == "Queen":
				return 12
			elif self.rank == "King":
				return 13
class Hand:
	def __init__(self):
		self.cards = []
		
	# ... methods from previous problems
	def add_card(self, Card):
		self.cards.append(Card)

	def remove_card(self, Card):
		if Card in self.cards:
			self.cards.remove(Card)
		
	
def sum_hand(hand):
	total = 0
	for card in hand.cards:
		value = card.get_value()
		if value == None:
			return None
		else:
			total += value
	return total

#test case
card_one = Card("Hearts", "3")     # 3
card_two = Card("Hearts", "Jack")  # 11
card_three = Card("Spades", "3")   # 3

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum_val = sum_hand(hand)
print(sum_val)  # Output: 17

