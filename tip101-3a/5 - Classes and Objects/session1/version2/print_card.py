"""
Step 1: Update the Card class with the new method print_card() provided below:

def print_card(self):
	print(f"{self.rank} of {self.suit}")
Step 2: Create an instance of the class and store it in a variable named card. 
The object should have suit "Clubs" and rank "Ace".

Step 3: Then, call the method print_card() on your card.

Expected Output: Ace of Clubs
"""
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print(f"{self.rank} of {self.suit}")
    

card = Card("Clubs", "Ace")

card.print_card()

