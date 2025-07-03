"""
Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:

Result Linked List would be: Mario -> Luigi -> Wario -> Toad

Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4.):

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)
Example Output:

Mario -> Luigi
Luigi -> Wario
Wario -> Toad
Toad -> None
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		

#i need to define them in reverse order otherwise it won't work
#deeper node needs to be defined first

node_4 = Node("Toad")
node_3 = Node("Wario", node_4)
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario", node_2)

#test case
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)


