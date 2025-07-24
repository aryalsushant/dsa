"""
Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

Evaluate the time complexity of your function.
"""
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def left_most(root):
	if not root:
		return None
	current = root
	while current.left != None:
		current = current.left
	return current.val

# === Test Case ===
# Tree structure:
#        1
#       / \
#      2   5
#     / \
#    4   3

tree = TreeNode(1,
	TreeNode(2,
		TreeNode(4),
		TreeNode(3)
	),
	TreeNode(5)
)

print("Expected: 4")
print("Result:", left_most(tree))