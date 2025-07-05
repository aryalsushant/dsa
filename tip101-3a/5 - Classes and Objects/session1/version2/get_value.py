"""
Problem 5: Get Value
Update the Card class with a new method get_value() that takes in no parameters except self.

The function returns the card's value depending on the card's rank:

If the card has rank 2, 3, 4, 5, 6, 7, 8, 9, 10, the method should return the rank as an integer
If the card has rank Ace, the method should return 1 as the card's value
If the card has rank Jack, the method should return 11 as the card's value
If the card has rank Queen, the method should return 12 as the card's value
If the card has rank King, the method should return 13 as the card's value
If the card is invalid, the method should return None
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

#test case
card = Card("Hearts", "7")
print(card.get_value())

card_two = Card("Spades", "Jack")
print(card_two.get_value())
		
	
	
		
    
			



