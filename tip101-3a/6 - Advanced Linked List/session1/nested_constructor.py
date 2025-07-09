"""
Step 1: Copy the following code into Replit.

Step 2: Add a line of code (outside of the class) to create the linked list 4 -> 3 -> 2 in a single assignment statement.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

head = Node(4, Node(3, Node(2)))
print(head.value)
print(head.next.value)
print(head.next.next.value)