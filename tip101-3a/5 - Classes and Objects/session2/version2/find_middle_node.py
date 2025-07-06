"""
Write a function find_middle_node() that takes in the head of a linked list and returns the "middle" node.

If the linked list has an even length and there are two "middle" nodes, return the first middle node.
(E.g., "1 -> 2 -> 3 -> 4" would return 2, not 3.)
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def find_middle_node(head):
	#we can solve this using two pointer technique
	#one pointer is slow and one is fast (double the speed)
	#when fast one reaches the end, slow one is at the middle
	#return slow
	fast = head
	slow = head
	while fast is not None and fast.next is not None and fast.next.next is not None:
		slow = slow.next
		fast = fast.next.next
	return slow

#test case
# Helper to build linked list from a list of values
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

# Helper to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# Test with odd-length list
print("Odd Length List:")
odd_list = build_linked_list([1, 2, 3, 4, 5])
print_linked_list(odd_list)
mid_node = find_middle_node(odd_list)
print("Middle node value (should be 3):", mid_node.value)

print("\nEven Length List:")
even_list = build_linked_list([1, 2, 3, 4])
print_linked_list(even_list)
mid_node = find_middle_node(even_list)
print("Middle node value (should be 2):", mid_node.value)
	
    
		