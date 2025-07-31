"""
Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, 
remove the node with the given key. Return the root of the modified tree.

The tree is sorted by key. If multiple nodes with the given key exist, remove the first node you find. 
If you need to remove a node with two children, use the in-order successor of that node, which is the 
smallest value in its right subtree. You do not need to maintain a balanced tree.

Evaluate the time complexity of your function.
"""
class TreeNode():
	def __init__(self, key, value, left=None, right=None):
		self.key = key
		self.val = value
		self.left = left
		self.right = right
		 
def remove_bst(root, key):
	# Locate the node to be removed
	if not root:
		return None
	if key < root.key:
		root.left = remove_bst(root.left, key)
	elif key > root.key:
		root.right = remove_bst(root.right, key)
	else:
		
	# If the node is a leaf node:
		if not root.left and not root.right:
			return None
		# Remove the node by redirecting the appropriate child reference of its parent to None
	# If the node has one parent:
		# Replace the node with its child, updating its parent's nodes child reference appropriately
		if not root.left:
			return root.right
		if not root.right:
			return root.left
	# If the node has two children:
		# Find the node's inorder successor (smallest node in right subtree)
		successor = root.right
		
		while successor.left:
			successor = successor.left
		# Swap the value of the node and its inorder successor
		root.key, root.val = successor.key, successor.val
		# Recursively remove the successor (which now has the current node's value)
		root.right = remove_bst(root.right, successor.key)
	# Return the root of the updated tree
	return root
