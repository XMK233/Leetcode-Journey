# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=117&&tqId=37757&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

判断平衡二叉树
剑指offer55II
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        root = pRoot
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if abs(left_depth - right_depth) <= 1:
            return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)
        else:
            return False

    def getDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))