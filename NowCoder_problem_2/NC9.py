class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

n1 = TreeNode(10)
n2 = TreeNode(5)
n3 = TreeNode(12)
n4 = TreeNode(4)
n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

# n1 = TreeNode(-2)
# n2 = TreeNode(-3)
# n1.right = n2

# n1 = TreeNode(1)
# n2 = TreeNode(3)
# n3 = TreeNode(4)
# n1.left = n2
# n1.right = n3

class Solution:
    def hasPathSum(self , root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.left == None and root.right == None and (sum - root.val) == 0:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


print(
    Solution().hasPathSum(n1, 22)
)