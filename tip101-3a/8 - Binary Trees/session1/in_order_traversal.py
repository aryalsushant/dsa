"""
Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. 
In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if not root:
        return []
    else:
        return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
