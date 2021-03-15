# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/da785ea0f64b442488c125b441a4ba4a?tpId=117&&tqId=37716&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个二叉树，请计算节点值之和最大的路径的节点值之和是多少。
这个路径的开始节点和结束节点可以是二叉树中的任意节点
例如：
给出以下的二叉树，

返回的结果为6
示例1
输入
复制
{-2,1}
返回值
复制
1
示例2
输入
复制
{-2,#,-3}
返回值
复制
-2

这题真的是好题. 看看代码吧, 看几遍就懂了, 方法很巧妙.
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
    def maxPathSum(self, root):
        # write code here
        self.res = float('-inf')  # 负无穷 这个是一个结果的记录点, 记录的是一棵树的结果. 而dfs函数返回的却是相当于一条链而非一棵树的结果.

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.res = max(self.res, root.val + l + r)
            return max(0, max(l, r) + root.val)

        _ = dfs(root)
        return self.res