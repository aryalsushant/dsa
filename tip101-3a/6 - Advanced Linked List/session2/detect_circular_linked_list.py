"""
A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, 
write a function is_circular() that returns True if the linked list is circular and False otherwise.

Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why 
you believe your solution has the stated time and space complexity.
"""
#idea: traverse thru linked list, get to the tail, if tail = head return True, else return False
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def is_circular(head):
	if head is None:
		return False
	
	current = head.next
	while current and current!= head:
		current = current.next
	return current == head

#test case

# Case 1: Circular list
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a  # back to head
print(is_circular(a))  # True

# Case 2: Not circular
x = Node(1, Node(2, Node(3)))
print(is_circular(x))  # False

# Case 3: Empty list
print(is_circular(None))  # False

# Case 4: Single node pointing to itself
n = Node(99)
n.next = n
print(is_circular(n))  # True

	