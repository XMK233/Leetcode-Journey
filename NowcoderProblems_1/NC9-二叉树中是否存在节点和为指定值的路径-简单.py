# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/508378c0823c423baa723ce448cbfd0c?tpId=117&&tqId=37719&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个二叉树和一个值\ sum sum，判断是否有从根节点到叶子节点的节点值之和等于\ sum sum 的路径，
例如：
给出如下的二叉树，\ sum=22 sum=22，

返回true，因为存在一条路径 5\to 4\to 11\to 25→4→11→2的节点值之和为 22
示例1
输入
复制
{1,2},0
返回值
复制
false
示例2
输入
复制
{1,2},3
返回值
复制
true

DFS和回溯算法。剑指offer34. 注意，剑指里面是找到路径，而这一题是要问你有没有这样的路径。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @param sum int整型
# @return bool布尔型
#

class Solution:
    def hasPathSum(self, root, sum):
        res, path = [], []

        def dfs(node, sum):
            # 递归出口：解决子问题
            if not node:
                return  # 如果没有节点(node = None)，直接返回，不向下执行
            else:  # 有节点
                path.append(node.val)  # 将节点值添加到path
                sum -= node.val
            # 如果节点为叶子节点，并且 sum == 0
            if not node.left and not node.right and not sum:
                res.append(path[:])

            dfs(node.left, sum)  # 递归处理左边
            dfs(node.right, sum)  # 递归处理右边
            path.pop()  # 处理完一个节点后，恢复初始状态，为node.left,  node.right操作

        dfs(root, sum)

        return len(res) > 0

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

n = buildTreeFromList([1, 2])
print(Solution().hasPathSum(n, 0))