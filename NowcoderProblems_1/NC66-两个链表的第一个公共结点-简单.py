# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=117&&tqId=37761&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

jianzhiOffer68II
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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