"""
Given the Pokemon class below, copy the code and add it to your Replit.

class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		pass
Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".

Example Usage:

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)
Example Output: "Pikachu dealt 20 damage to Bulbasaur"

"""
class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		p1 = self.damage
		p2 = opponent.hp
		if p2-p1 <= 0:
			print(opponent.name, " fainted")
		else:
			print(self.name, " dealt ", self.damage, " damage to ", opponent.name )

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)