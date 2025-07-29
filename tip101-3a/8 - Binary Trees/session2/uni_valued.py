"""
A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, 
return True if the given tree is uni-valued and False otherwise.

Evaluate the time complexity of your solution.
"""
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
         
def is_univalued(root):
    def make_list(root):
        if not root:
            return []
        else:
            return make_list(root.left)+[root.val]+make_list(root.right)
    
    lst = make_list(root)
    return len(set(lst)) <= 1


# Test case 1: Uni-valued tree
#       1
#      / \
#     1   1
#    / \
#   1   1
tree1 = TreeNode(1,
         TreeNode(1,
             TreeNode(1),
             TreeNode(1)
         ),
         TreeNode(1))

print(is_univalued(tree1))  # Output: True

# Test case 2: Not uni-valued tree
#       2
#      / \
#     2   3
tree2 = TreeNode(2,
         TreeNode(2),
         TreeNode(3))

print(is_univalued(tree2))  # Output: False

# Test case 3: Single node tree
tree3 = TreeNode(7)
print(is_univalued(tree3))  # Output: True

# Test case 4: Empty tree
print(is_univalued(None))  # Output: True