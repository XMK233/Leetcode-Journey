# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/185a87cd29eb42049132aed873273e83?tpId=117&&tqId=37715&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个仅包含数字\ 0-9 0−9 的二叉树，每一条从根节点到叶子节点的路径都可以用一个数字表示。
例如根节点到叶子节点的一条路径是1\to 2\to 31→2→3,那么这条路径就用\ 123 123 来代替。
找出根节点到叶子节点的所有路径表示的数字之和
例如：

这颗二叉树一共有两条路径，
根节点到叶子节点的路径 1\to 21→2 用数字\ 12 12 代替
根节点到叶子节点的路径 1\to 31→3 用数字\ 13 13 代替
所以答案为\ 12+13=25 12+13=25
示例1
输入
复制
{1,0}
返回值
复制
10
示例2
输入
复制
{1,#,9}
返回值
复制
19

这道题有助于我们获得经验：如何将一棵树里面从根到叶所有的路径都存下来。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # def pathSum(self, root: TreeNode, sum: int):
    def sumNumbers(self, root):
        # write code here
        res, path = [], []
        def dfs(node):
            #递归出口：解决子问题
            if not node:
                return #如果没有节点(node = None)，直接返回，不向下执行
            else:               #有节点
                path.append(str(node.val)) #将节点值添加到path
                # sum -= node.val
            # 如果节点为叶子节点，并且 sum == 0
            if not node.left and not node.right:
                res.append(int("".join(path)))

            dfs(node.left) #递归处理左边
            dfs(node.right) #递归处理右边
            path.pop() #处理完一个节点后，恢复初始状态，为node.left,  node.right操作

        dfs(root)
        return sum(res)


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

tree = buildTreeFromList([1, 0])
print(Solution().sumNumbers(tree))