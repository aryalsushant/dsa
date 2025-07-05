"""
Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the 
string " -> " to separate each node.

Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	current = head
	result = []
	while current is not None:
		result.append(current.value)
		current = current.next
	print (" -> ".join(result))


#test case
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")

# Link the nodes
a.next = b
b.next = c
c.next = d
d.next = e

# Test it
print_linked_list(a)


