"""
Given the root of a binary search tree, write a function descending_leaves() that returns a list of the values of 
all leaves in the BST in descending order. Assume the tree is balanced.
"""
class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   
def descending_leaves(root):
    if not root:
        return []
    if root.left is None and root.right is None:
        return [root.val]
    else:
        return sorted(descending_leaves(root.left)+descending_leaves(root.right), reverse = True)

# Build this BST:
#         4
#        / \
#       2   6
#      / \   \
#     1   3   7

tree = TreeNode(4,
        TreeNode(2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(6,
            None,
            TreeNode(7)
        )
    )

print(descending_leaves(tree))  # Output should be [7, 3, 1]

# Additional test case: single-node tree
single = TreeNode(10)
print(descending_leaves(single))  # Output: [10]

# Empty tree
print(descending_leaves(None))  # Output: []