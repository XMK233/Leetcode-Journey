# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### https://blog.csdn.net/coder_orz/article/details/51335758
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if abs(left_depth - right_depth) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def getDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

## 思路很简单.
## 左右子树皆是平衡二叉树, 并且自己也是平衡二叉树(左右子树的搞毒相差不超过1)