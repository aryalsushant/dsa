"""
Write a function print_reverse() that takes in the tail of a doubly linked list as a parameter.

It should print out the values of the linked list in reverse order, each separated by a space.
"""
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def print_reverse(tail):
	current = tail
	result = [str(tail.value)]
	while current.prev:
		result.append(str(current.prev.value))
		current = current.prev
	print(" ".join(result))

#test case
poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl")
poliwrath = Node("Poliwrath")

poliwag.next = poliwhirl
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl
poliwhirl.prev = poliwag

print_reverse(poliwrath)
	

