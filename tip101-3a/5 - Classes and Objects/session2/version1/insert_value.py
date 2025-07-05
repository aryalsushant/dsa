"""
Write a function ll_insert() that takes in a head of a linked list, a value val, and an index i as parameters.

The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.

If i is greater than the length of the list, insert the new node at the end of the list.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.

"""
#two edge cases: i is 0 or i is greater than length of list
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
	
	
	new_node = Node(val)
	
    #0
	if i == 0:
		new_node.next = head
		return new_node
	
    #last ma
	
		
	#last ma insert garne
	count = 0
	current = head
	while current != None and count < i-1:
		current = current.next
		count +=1
	if current is None:
		if head is None:
			return new_node #this means list was empty
		tail = head
		while tail.next != None:
			tail = tail.next
		tail.next = new_node
		return head
			
	#bich ma insert garne
	new_node.next=current.next
	current.next = new_node
	return head

# -------- TEST CASES -------- (thanks to chatgpt)

# Create list: 1 -> 2 -> 4
n3 = Node(4)
n2 = Node(2, n3)
n1 = Node(1, n2)
head = n1

# Test 1: Insert 3 at index 2 => 1 -> 2 -> 3 -> 4
head = ll_insert(head, 3, 2)

# Test 2: Insert 0 at index 0 => 0 -> 1 -> 2 -> 3 -> 4
head = ll_insert(head, 0, 0)

# Test 3: Insert 99 at index 100 (too large) => 0 -> 1 -> 2 -> 3 -> 4 -> 99
head = ll_insert(head, 99, 100)

# Function to print the final list
def print_list(head):
	current = head
	while current:
		print(current.value, end=" -> ")
		current = current.next
	print("None")

# Run the print
print_list(head)

# Expected output:
# 0 -> 1 -> 2 -> 3 -> 4 -> 99 -> None
	
	
	

	
	

	

	
	

		
	