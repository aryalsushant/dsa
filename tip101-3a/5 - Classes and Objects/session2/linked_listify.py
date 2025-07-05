"""
Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list.
 The function should return the head of the linked list.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def list_to_linked_list(lst):
	
	head = Node(lst[0])
	current = head
	
	for item in lst[1:]:
		current.next = Node(item)
		current = current.next
	
	return head
#helper functipon to print linked list
def print_linked_list(head):
	current = head
	result = []
	while current is not None:
		result.append(current.value)
		current = current.next
	result.append("None")
	print (" -> ".join(result))

#test case
normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print_linked_list(linked_list)
	
		