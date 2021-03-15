# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/47e1687126fa461e8a3aff8632aa5559?tpId=117&&tqId=37722&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
例如：
给定的二叉树是{3,9,20,#,#,15,7},

该二叉树之字形层序遍历的结果是
[
[3],
[20,9],
[15,7]
]
示例1
输入
复制
{1,#,2}
返回值
复制
[[1],[2]]

剑指offer32III
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        ## 如果root为空:
        if root == None:
            return []
        ## 如果root是一个普通的数:
        res = []
        ### 初始化方向和当前层的最后一个节点:
        order = "leftToRight"
        bidirectionalQueue = [root]
        resCurLevel = []
        lastNodeOfThisLevel = bidirectionalQueue[-1] #root
        while len(bidirectionalQueue) != 0:
            if order == "leftToRight":
                ## 从左边吐出
                _ = bidirectionalQueue.pop(0)
                # if _ == None:
                #     continue
                resCurLevel.append(_.val)
                if _.left != None:
                    bidirectionalQueue.append(_.left)
                if _.right != None:
                    bidirectionalQueue.append(_.right)
                if _ == lastNodeOfThisLevel:
                    order = "rightToLeft"
                    res.append(resCurLevel)
                    resCurLevel = []
                    if len(bidirectionalQueue) != 0:
                        lastNodeOfThisLevel = bidirectionalQueue[0]
            else:
                ## 从右边吐出
                _ = bidirectionalQueue.pop(-1)
                # if _ == None:
                #     continue
                resCurLevel.append(_.val)
                if _.right != None:
                    bidirectionalQueue.insert(0, _.right)
                if _.left != None:
                    bidirectionalQueue.insert(0, _.left)
                if _ == lastNodeOfThisLevel:
                    order = "leftToRight"
                    res.append(resCurLevel)
                    resCurLevel = []
                    if len(bidirectionalQueue) != 0:
                        lastNodeOfThisLevel = bidirectionalQueue[-1]

        return res