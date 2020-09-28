# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ## 边界条件
        if root == None:
            return None
        ## 如果有一个点直接就是root, 那么就直接返回root即可啦.
        if root == p or root == q:
            return root
        ## 剩下的情况就是比较复杂的普通情况了.
        ### 情况1: p,q一大一小于root, 分居两侧, 那么root就是共祖.
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        ### 情况2: 都小于
        elif p.val < root.val and q.val < root.val: # (p.val + q.val) < 2 * root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        ### 情况3: 都大于
        elif p.val > root.val and q.val > root.val: # (p.val + q.val) > 2 * root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return None

