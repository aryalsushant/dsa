"""
Step 1: Using the Player class from Problem 1, add the following get_player() method to your Replit code:

def get_player(self):
	return f"{self.character} driving the {self.kart}"
Step 2: Create a second instance of Player in a variable named player_two.

The Player object created should have character "Bowser" and kart "Pirahna Prowler".
Step 3: Use the method get_player() below to print out "Match: Yoshi driving the Super Blooper vs Bowser 
driving the Pirahna Prowler".
"""
class Player():
	def  __init__(self, character, kart):
		self.character = character
		self.kart = kart
		self.items = []
	
	def get_player(self):
		return f"{self.character} driving the {self.kart}"
	
player_one = Player("Yoshi", "Super blooper")
player_two = Player("Bowser", "Piranha Prowler")


print(player_one.character, " driving", player_one.kart, " vs ", player_two.character, " vs ", player_two.kart)
print(player_one.get_player(), " vs ", player_two.get_player())