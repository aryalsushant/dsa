"""
Building off the Node class from Problem 9, now we will link the nodes together.

To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9
to point to node_two.

Example Usage (after updating node_one's next property):
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		

node_two = Node("b")
node_one = Node("a", node_two)

#test case

print(node_one.value)
print(node_one.next.value)
print(node_two.value)