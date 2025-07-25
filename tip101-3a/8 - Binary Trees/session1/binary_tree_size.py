"""
Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

Evaluate the time complexity of your function.


"""
class TreeNode():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
   
def size(root):
	if not root:
		return 0
	else:
		return 1 + size(root.left) +size(root.right)
	
# Tree:
#     1
#    / \
#   2   3
#  /
# 4

tree = TreeNode(1,
	TreeNode(2, TreeNode(4)),
	TreeNode(3)
)

print("Expected: 4")
print("Result:", size(tree))

# Build the tree:
#         10
#        /  \
#       5    15
#      / \   / \
#     2   7 12  20

tree = TreeNode(10,
        TreeNode(5,
            TreeNode(2),
            TreeNode(7)
        ),
        TreeNode(15,
            TreeNode(12),
            TreeNode(20)
        )
    )

print("Expected: 7")
print("Result:", size(tree))

