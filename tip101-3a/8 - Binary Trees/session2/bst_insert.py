"""
Given the root of a binary search tree, insert a new node with a given key and value into the tree. 
Return the root of the modified tree. The tree is sorted by key. If a node with the given key already exists, 
update the the existing key’s value. You do not need to maintain a balanced tree.

Evaluate the time complexity of your function.
"""
class TreeNode():
	def __init__(self, key, value, left=None, right=None):
		self.key = key
		self.val = value
		self.left = left
		self.right = right
   
def insert(root, key, value):
	if not root:
		return TreeNode(key, value)
	if key < root.key:
		root.left = insert(root.left, key, value)
	elif key > root.key:
		root.right = insert(root.right, key, value)
	else:
		root.val = value
	return root

# Helper function to print tree in-order
def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(f"Key: {node.key}, Value: {node.val}")
    print_inorder(node.right)

# Build initial tree:
#         10
#        /  \
#       5    15
#      / \
#     1   6

root = TreeNode(10, "Root")
root.left = TreeNode(5, "Left")
root.right = TreeNode(15, "Right")
root.left.left = TreeNode(1, "One")
root.left.right = TreeNode(6, "Six")

# Insert new node
root = insert(root, 9, "Naruto")  # New node
root = insert(root, 5, "Updated Left")  # Update existing node

# Print tree to verify
print("In-order traversal after insertions:")
print_inorder(root)