"""
Write a function ll_pop() that takes in the head of a linked list and an index i as parameters.

The function should remove the node at index i of the linked list and return the head of the list.

If i is greater than the length of the list, do nothing.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_pop(head, i):
	#when count reaches i-1, we skip the next node
	# and connect the current directly to current.next.nexr
	if i == 0:
		return head.next #removing the head node if i = 0
	current = head
	count = 0
	while current is not None and current.next is not None:
		if current == i-1:
			current.next = current.next.next
			return head
		current = current.next
		count += 1
	return head #if i is greater than count, return as it is



