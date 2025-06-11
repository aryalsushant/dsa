"""
write a function that takes a dictionary and a key.
looks for the target, when found, prints key and its associated value
If target is not in dictionary, print "That pair does not exist!"

1. if target not in dictionary, print the pair does not exist
2. iterate through the loop
3. look for target
"""

def print_pair(dictionary, target):
    if target not in dictionary:
        print("The pair does not exist")
    else:
        
        print("Key:", target)
        print("Value:",dictionary[target])

#test case
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")



