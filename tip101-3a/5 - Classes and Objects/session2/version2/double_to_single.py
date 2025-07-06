"""
Below are the node classes for a singly linked list and a doubly linked list. Write a function dll_to_sll() 
that takes in the head of a doubly linked list as a parameter and recreates it as a singly linked list.

The function returns the head of the new singly linked list.
"""
class SLLNode:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

class DLLNode:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
		
def dll_to_sll(dll_head):
	#if linked list is empty then return none
	if dll_head is None:
		return None
	sll_head = SLLNode(dll_head.value)
	
	current_sll = sll_head
	current_dll = dll_head.next
	while current_dll:
		new_node = SLLNode(current_dll.value)
		current_sll.next = new_node
		current_sll = current_sll.next
		current_dll=current_dll.next
	return sll_head

#test case
# Create DLL: Ice <-> Water <-> Steam
steam = DLLNode("Steam")
water = DLLNode("Water", next=steam)
steam.prev = water
ice = DLLNode("Ice", next=water)
water.prev = ice

dll_head = ice
sll_head = dll_to_sll(dll_head)

# Print SLL to check
current = sll_head
while current:
    print(current.value, end=" -> ")
    current = current.next
# Output: Ice -> Water -> Steam -> 
