# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/8a2b2bf6c19b4f23a9bdb9b233eefa73?tpId=117&&tqId=37721&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

二叉树最大深度. 剑指offer15I
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @return int整型
#
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))