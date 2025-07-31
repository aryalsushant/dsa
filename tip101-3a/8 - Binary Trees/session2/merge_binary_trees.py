"""
You are given two binary trees with roots root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the 
others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap,
 then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of
   the new tree.

Return the merged tree.
"""
class TreeNode:
	def __init__(self, val = 0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:	
    def merge_trees(self, root1, root2):
        if not root1 and not root2:
            return None
        elif root1 and not root2:
            return root1
        elif root2 and not root1:
            return root2
        
        merged = TreeNode(root1.val+root2.val) #creating the sum of values of two nodes
        merged.left = self.merge_trees(root1.left, root2.left)
        merged.right = self.merge_trees(root1.right, root2.right)

        return merged
# Helper function to print tree in-order
def print_inorder(root):
	if not root:
		return
	print_inorder(root.left)
	print(root.val, end=' ')
	print_inorder(root.right)

# Construct Tree 1
#      1
#     / \
#    3   2
#   /
#  5
t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

# Construct Tree 2
#      2
#     / \
#    1   3
#     \   \
#      4   7
t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)

# Merge and print
solution = Solution()
merged = solution.merge_trees(t1, t2)

print("Inorder traversal of merged tree:")
print_inorder(merged)