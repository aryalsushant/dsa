"""
Given a value and the root of a tree, write a function find() that returns True if there is a node with the given 
value in the tree. Assume the tree is balanced.

Evaluate the time complexity of your solution.
"""
class TreeNode():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
   
def find(root, value):
	if root is None:
		return False
	if root.val == value:
		return True
	else:
		return find(root.left, value) or find(root.right, value)
	  
# Build this tree:
#         1
#        / \
#       2   5
#      / \
#     4   3

tree = TreeNode(1,
        TreeNode(2,
            TreeNode(4),
            TreeNode(3)
        ),
        TreeNode(5)
    )

# Test cases
print(find(tree, 5))   # True
print(find(tree, 3))   # True
print(find(tree, 10))  # False
print(find(tree, 1))   # True
print(find(tree, 6))   # False