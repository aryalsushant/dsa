"""
Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original 
and
replacement as parameters.

The function updates any node with value original to have value replacement.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	current = head
	while current != None:
		if current.value == original:
			current.value = replacement
		current = current.next

#questio doesnt ask to return anything so this should be it
		

