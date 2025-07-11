"""
Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.

The function returns a list of values of the first n nodes.

If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
"""
#create an empty list
#start at the head node
#use a while loop to add the current node's value
#stop if you've added n values or you've run out of nodes
#return the list
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	result = []
	current = head
	while current != None and len(result) < n:
		result.append(current.value)
		current = current.next
	return result

#test case generated by chatgpt
# Create a linked list: a -> b -> c
node_c = Node("c")
node_b = Node("b", node_c)
node_a = Node("a", node_b)

# Test the function with n = 2
head = node_a
lst = listify_first_n(head, 2)
print(lst)  # Expected output: ['a', 'b']

# Bonus: Test the function with n = 5 (greater than list length)
lst2 = listify_first_n(head, 5)
print(lst2)  # Expected output: ['a', 'b', 'c']