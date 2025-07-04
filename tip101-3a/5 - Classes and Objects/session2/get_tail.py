"""
Write a function get_tail() that takes in the head of a linked list as a parameter.

It should print out the value of the tail of the list.

If the list is empty (head is None), return None.
Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	current = head
	while current.next != None:
		current = current.next
	return current.value


# Create nodes manually: num1 -> num2 -> num3
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)

# Assign head
head = num1

# Call the function
tail = get_tail(head)

# Print result
print(tail)  # Expected Output: num3
