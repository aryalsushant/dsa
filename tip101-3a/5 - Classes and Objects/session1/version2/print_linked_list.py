"""
Write a function print_linked_list() that takes in a head of a linked list as a parameter. 
The function prints and returns a list of all the values in the linked list in the order they appear in the linked list.

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
		
		print(current.value)
		result.append(current.value)
		current = current.next
		
	return result
		

#test case
node3 = Node(30)
node2 = Node(20, node3)
node1 = Node(10, node2)

print(print_linked_list(node1))
