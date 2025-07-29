"""
Given the root of a binary tree, write a function height() that returns the height of a binary tree.

Evaluate the time complexity of your function.
"""
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
   
def height(root):
    if not root:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))
    
# Test case 1
#         4
#        / \
#       2   5
#      / \
#     1   3
tree1 = TreeNode(4,
         TreeNode(2,
             TreeNode(1),
             TreeNode(3)
         ),
         TreeNode(5))

print(height(tree1))  # Output: 3

# Test case 2: Single node
tree2 = TreeNode(7)
print(height(tree2))  # Output: 1

# Test case 3: Empty tree
print(height(None))   # Output: 0
