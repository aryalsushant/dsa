"""
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, 
return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.
"""
class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def check_tree(root):
	if root.val == root.left.val + root.right.val:
		return True
	else:
		return False
