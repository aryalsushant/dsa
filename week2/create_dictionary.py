"""
we take a list of keys and a list of values as inputs
output should be a dictionary containing the corresponding keys and values

"""

'''
def create_dictionary(keys, values):
    dictionary = {}
    for key in keys:
        for value in values:
            dictionary[key]=value
    return dictionary

#EXAMPLE INPUT
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values)) does not work

'''

def create_dictionary(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]]=values[i]
    return dictionary

#EXAMPLE INPUT
keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))
