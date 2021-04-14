# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/e0cc33a83afe4530bcec46eba3325116?tpId=117&&tqId=37826&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一棵二叉树以及这棵树上的两个节点 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。
示例1
输入
复制
[3,5,1,6,2,0,8,#,#,7,4],5,1
返回值
复制
3

jianzhiOffer68II
'''
class Solution:
    def lowestCommonAncestor(self , root , o1 , o2 ):
        # write code here
        def dfs(root, o1, o2):
            if not root:
                return None
            if root.val ==o1 or root.val==o2:
                return root
            left = dfs(root.left, o1, o2)
            right = dfs(root.right, o1, o2)
            if not left:
                return right
            if not right:
                return left
            return root
        return dfs(root, o1, o2).val