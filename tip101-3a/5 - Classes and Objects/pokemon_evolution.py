"""
Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon 
has an attribute evolution. The attribute will either be the default value of None or another Pokemon instance.

Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.
"""
class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
 
def get_evolutionary_line(starter_pokemon):
	result =[starter_pokemon.name]
	current = starter_pokemon
	while current.evolution != None:
		result.append(current.evolution.name)
		current = current.evolution
	return result
		
	

#test cases
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)