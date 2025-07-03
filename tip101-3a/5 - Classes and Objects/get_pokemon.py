"""
Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon 
and a string pokemon_type as parameters.

The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

Hint: To test, loop over Pokemon in return list and print the Pokemon's name
"""
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    
    def choose(self):
        if self.is_caught == True:
            print(self.name, " I choose you!")
        else:
            print(self.name, " is wild! Catch them if you can!")
    
    def catch(self):
        self.is_caught = True
    
    def add_type(self, new_type):
        self.types.append(new_type)

#this time im not defining a method but a function
def get_by_type(my_pokemon, pokemon_type):
    result = []
    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            result.append(pokemon)
    return result

        

#test case
# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
for p in normal_pokemon:
    print(p.name)