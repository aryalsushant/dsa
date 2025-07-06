"""
In poker, players are given a hand of five cards. A player has a "two-pair" hand if they have two cards of 
the same rank and another two cards of another rank. The fifth card isn’t used here.

Given the Card class below, write a function is_two_pair() that takes in a list player_hand that contains 5 Card objects.

The function returns True if the player has a two pair hand and False otherwise.

Cards in the hand are guaranteed to be unique and are guaranteed to have on the following suits and ranks:

The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
"""
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def is_two_pair(player_hand):
	uniques = []
	for hand in player_hand:
		if hand.rank in uniques:
			pass
		else:
			uniques.append(hand.rank)
	if len(uniques) ==1 or len(uniques) == 3:
		#print(uniques)
		return True
	else:
		#print(uniques)
		return False
		
	
		

#test case
card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))

"""
example output
True  # Two Aces + Two 4s (+ Unused 6)
False # Two 4s (+ Ace + 6 + 7)
"""