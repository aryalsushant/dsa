"""
Update the Card class with a new method is_valid() that takes in no parameters except self. 
The method should return True if:

The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", 
"Queen", "King", "Ace"
"""
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	
	def is_valid(self):
		suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
		ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
		if self.suit in suits and self.rank in ranks:
			return True
		else:
			return False
		
#test case
my_card = Card("Hearts", "7")
print(my_card.is_valid())

second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())
		