# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/04a5560e43e24e9db4595865dc9c63a3?tpId=117&&tqId=37723&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
例如：
给定的二叉树是{3,9,20,#,#,15,7},

该二叉树层序遍历的结果是
[
[3],
[9,20],
[15,7]
]
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def levelOrder(self, root):
        ## 如果root为空:
        if root == None:
            return []
        ## 如果root是一个普通的数:
        res = []
        ### 初始化方向和当前层的最后一个节点:
        # order = "leftToRight"
        bidirectionalQueue = [root]
        resCurLevel = []
        lastNodeOfThisLevel = bidirectionalQueue[-1] #root
        while len(bidirectionalQueue) != 0:
            # if order == "leftToRight":
            ## 从左边吐出
            _ = bidirectionalQueue.pop(0)
            resCurLevel.append(_.val)
            ## 然后, 把刚吐出的节点的左,右节点往bidirectionalQueue的右边怼进去
            if _.left != None:
                bidirectionalQueue.append(_.left)
            if _.right != None:
                bidirectionalQueue.append(_.right)
            ## 如果这个时候, 当前层遍历到了最后一个节点了, 就要进入下一层\换方向\填充res数组之类的一系列操作了.
            if _ == lastNodeOfThisLevel:
                # order = "rightToLeft"
                res.append(resCurLevel)
                resCurLevel = []
                if len(bidirectionalQueue) != 0:
                    ## 当前层遍历完之后, bidirectionalQueue里面就全部是下一层的点了, 所以下一层的最后一个吐出的节点将会是左边第一个点
                    lastNodeOfThisLevel = bidirectionalQueue[-1]
        return res