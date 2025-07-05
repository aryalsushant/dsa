"""
Step 1: Copy the following code into Replit.

Step 2: Instantiate an instance of the class Card and store it in a variable named card.
The Card object should have the suit "Spades" and the rank "8".
"""
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

card = Card("Spades", "8")