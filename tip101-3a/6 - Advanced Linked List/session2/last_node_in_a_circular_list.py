"""
Given the head of a singly linked list, write a function that returns the last node in the cycle. 
If there is no cycle in the linked list, return None.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def find_last_node_in_cycle(head):
	if head is None:
		return None
	
	current = head.next
	while current and current!= head:
		current = current.next
	is_circular = (current == head)
	new_current = head
	if is_circular:
		while current and current.next!=head:
			current = current.next
		return current
	else:
		return None
		


#test cases
# Case 1: Circular list
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a
print(find_last_node_in_cycle(a).value)  # Output: 3

# Case 2: Non-circular
x = Node(1, Node(2, Node(3)))
print(find_last_node_in_cycle(x))  # Output: None

# Case 3: Single node pointing to itself
n = Node(99)
n.next = n
print(find_last_node_in_cycle(n).value)  # Output: 99

# Case 4: Empty list
print(find_last_node_in_cycle(None))  # Output: None
