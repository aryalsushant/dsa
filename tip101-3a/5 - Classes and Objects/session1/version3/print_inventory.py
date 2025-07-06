"""
Update the Player class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a player’s items list.

If the player has no items, the function should print "Inventory empty".
"""
class Player():
	def __init__(self, character, kart):
		self.character = character
		self.kart = kart
		self.items = []

	def add_item(self, item_name):
		valid_items = [
			"banana", "green shell", "red shell", "bob-omb",
			"super star", "lightning", "bullet bill"
		]
		if item_name in valid_items:
			self.items.append(item_name)

	def print_inventory(self):
		hash = {}
		if len(self.items) == 0:
			print("Inventory empty")
		else:
			for saman in self.items:
				if saman not in hash:
					hash[saman] = 1
				else:
					hash[saman] += 1
			return hash


#test case
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]


print(player_one.print_inventory())
