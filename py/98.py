# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## https://blog.csdn.net/fuxuemingzhu/article/details/70209865
## 我自己的思路有点复杂, 要判断一棵子树是不是搜索树, 还要返回这个搜索树的最小值和最大值.
## 看看人家的思路, 真心很不错.

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, min, max):
        if not root: return True
        if root.val >= max or root.val <= min:
            return False
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)