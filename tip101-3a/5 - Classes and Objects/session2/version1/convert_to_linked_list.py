"""
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. 
The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they 
appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element 
in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be 
stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or
 pointer to the next node in the list.

Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		

node_2 = Node("Jigglybuff")
node_1 = Node("Wigglypuff", node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

