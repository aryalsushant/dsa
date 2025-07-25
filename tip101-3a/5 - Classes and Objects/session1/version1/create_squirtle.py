"""
Step 1: Add the print_pokemon definition below to your code on Replit.

Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. 
The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. 
Use the print_pokemon() function to verify that squirtle's is_caught property was updated.
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
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.is_caught = False
squirtle.print_pokemon()