# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/840dd2dc4fbd4b2199cd48f2dadf930a?tpId=117&&tqId=37718&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个二叉树和一个值\ sum sum，请找出所有的根节点到叶子节点的节点值之和等于\ sum sum 的路径，
例如：
给出如下的二叉树，\ sum=22 sum=22，

返回
[
[5,4,11,2],
[5,8,9]
]
示例1
输入
复制
{1,2},1
返回值
复制
[]
示例2
输入
复制
{1,2},3
返回值
复制
[[1,2]]

'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @param sum int整型
# @return int整型二维数组
#
class Solution:
    def pathSum(self , root , sum ):
        res, path = [], []

        def dfs(node, sum):
            #递归出口：解决子问题
            if not node: return #如果没有节点(node = None)，直接返回，不向下执行
            else:               #有节点
                path.append(node.val) #将节点值添加到path
                sum -= node.val
            # 如果节点为叶子节点，并且 sum == 0
            if not node.left and not node.right and not sum:
                res.append(path[:])

            dfs(node.left, sum) #递归处理左边
            dfs(node.right, sum) #递归处理右边
            path.pop() #处理完一个节点后，恢复初始状态，为node.left,  node.right操作. ## 这一步就体现了回溯

        dfs(root, sum)
        return res