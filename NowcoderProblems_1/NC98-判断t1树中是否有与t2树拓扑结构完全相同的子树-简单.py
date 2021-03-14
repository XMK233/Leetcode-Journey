# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/4eaccec5ee8f4fe8a4309463b807a542?tpId=117&&tqId=37821&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
'''
题目描述
给定彼此独立的两棵二叉树，判断 t1 树是否有与 t2 树拓扑结构完全相同的子树。
设 t1 树的边集为 E1，t2 树的边集为 E2，若 E2 等于 E1 ，则表示 t1 树和t2 树的拓扑结构完全相同。
示例1
输入
复制
{1,2,3,4,5,6,7,#,8,9},{2,4,5,#,8,9}
返回值
复制
true
备注:
1 \leq n \leq 5000001≤n≤500000
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root1 TreeNode类
# @param root2 TreeNode类
# @return bool布尔型
#
class Solution:
    def isContains(self , root1 , root2 ):
        ## either of them are empty:
        if root1 == None: return False
        if root2 == None: return True
        ## root1 and root2 are not empty:
        # def isSubTree(r1, r2):
        #     if r1 == None and r2 == None:
        #         return True
        #     if r1 == None or r2 == None or r1.val != r2.val:
        #         return False
        #     return isSubTree(r1.left, r2.left) and isSubTree(r1.right, r2.right)
        def isTheSame(r1, r2):
            if r1 == None and r2 == None:
                return True
            if r1 == None or r2 == None:
                return False
            if r1.val != r2.val:
                return False
            return isTheSame(r1.left, r2.left) and isTheSame(r1.right, r2.right)
        if root1.val == root2.val:
            ## 这个判断这边犯过两个错：
            ### 1. return的东西太少了。凭什么root1与root2的值不同，就直接返回false？后面不再拯救一下？
            ### 2.最早写的时候，是写的root1==root2，应该是两个点的val相等与否啊，这种错误老是犯，你可还行？
            return isTheSame(root1, root2) or self.isContains(root1.left, root2) or self.isContains(root1.right, root2)
        else:
            return self.isContains(root1.left, root2) or self.isContains(root1.right, root2)

def buildTreeFromList(l):
    l_node = []
    for _ in l:
        if _ == "#":
            l_node.append(None)
        else:
            l_node.append(TreeNode(_))
    i = 0
    while i < len(l_node):
        if l_node[i] == None:
            pass
        else:
            if i * 2 + 1 < len(l_node):
                l_node[i].left = l_node[i * 2 + 1]
            if i * 2 + 2 < len(l_node):
                l_node[i].right = l_node[i * 2 + 2]
        i += 1
    return l_node[0]

a = buildTreeFromList([1,2,3,4,5,6,7,"#",8,9])
b = buildTreeFromList([2,4,5,"#",8,9])
print(Solution().isContains(a, b))

