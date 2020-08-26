# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        tmp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tmp)
        return root

n4 = TreeNode(4)
n2 = TreeNode(2)
n7 = TreeNode(7)
n1 = TreeNode(1)
n3 = TreeNode(3)
n6 = TreeNode(6)
n9 = TreeNode(9)
n4.left = n2
n4.right = n7
n2.left = n1
n2.right = n3
n7.left = n6
n7.right = n9

s = Solution()
reverted = s.invertTree(n4)
print(reverted)
