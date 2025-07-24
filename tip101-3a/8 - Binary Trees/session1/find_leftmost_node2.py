"""
If you implemented the previous left_most() function iteratively, implement it recursively.
 If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of the function.
"""
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def left_most(root):
	if not root:
		return None
	
	if not root.left:
		return root.val
	else:
		return left_most(root.left)
	
# Test Tree:
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