"""
Given a value and the root of a binary search tree, write a function find_bst() that returns True if
 there is a node with the given value in the tree. Assume the tree is balanced.
"""
class TreeNode():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
   
def find_bst(root, value):
	if not root:
		return False
	if root.val == value:
		return True
	elif value < root.val:
		return find_bst(root.left, value)
	else:
		return find_bst(root.right, value)

# Build this BST:
#         4
#        / \
#       2   5
#      / \
#     1   3

tree = TreeNode(4,
        TreeNode(2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(5)
    )

# Test cases
print(find_bst(tree, 5))   # True
print(find_bst(tree, 3))   # True
print(find_bst(tree, 10))  # False
print(find_bst(tree, 1))   # True
print(find_bst(tree, 0))   # False