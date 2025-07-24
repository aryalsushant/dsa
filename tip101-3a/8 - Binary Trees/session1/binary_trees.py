class TreeNode:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, key):
        self.value = key
        self.next = None

# create the root node
root = TreeNode(13)

# create the left subtree
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)

# create the right subtree
root.right = TreeNode(21)
root.right.left = TreeNode(15)
root.right.right = TreeNode(24)
root.right.right.right = TreeNode(26)