"""
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about 
the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a 
prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Given the Node class for a doubly linked list below, recreate the list ["Poliwag", "Poliwhirl", "Poliwrath"] as a 
doubly linked list.
"""
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev

poliwag = Node("Poliwag")
poliwhirl = Node("Poliwhirl")
poliwrath = Node("Poliwrath")

poliwag.next = poliwhirl
poliwhirl.next = poliwrath
poliwrath.prev = poliwhirl
poliwhirl.prev = poliwag

#test case
print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
