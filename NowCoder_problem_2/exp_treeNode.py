class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# n1 = TreeNode(-20)
# n2 = TreeNode(8)
# n3 = TreeNode(20)
# n4 = TreeNode(15)
# n5 = TreeNode(6)
# n1.left = n2
# n1.right = n3
# n3.left = n4
# n3.right = n5

# n1 = TreeNode(-2)
# n2 = TreeNode(-3)
# n1.right = n2

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3