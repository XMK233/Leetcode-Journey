# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/1b0b7f371eae4204bc4a7570c84c2de1?tpId=117&&tqId=37724&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一棵二叉树，判断琪是否是自身的镜像（即：是否对称）
例如：下面这棵二叉树是对称的
     1
    /  \
  2    2
 / \    / \
3 4  4  3
下面这棵二叉树不对称。
    1
    / \
  2   2
    \    \
    3    3
备注：
希望你可以用递归和迭代两种方法解决这个问题

剑指offer28
'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @return bool布尔型
#
class Solution:
    def twoSubTreesAreSymmetric(self, root1, root2):
        ## 二大皆空
        if root1 == root2 == None:
            return True
        ## 一者为空
        if root1 == None and root2 != None or root1 != None and root2 == None:
            return False
        ## 二大皆不空且二者值不同
        if root1.val != root2.val:
            return False
        ## 二大皆不空且二者值相同，那就要递归了
        return self.twoSubTreesAreSymmetric(root1.left, root2.right) and self.twoSubTreesAreSymmetric(root1.right, root2.left)


    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        ##
        return self.twoSubTreesAreSymmetric(root.left, root.right)