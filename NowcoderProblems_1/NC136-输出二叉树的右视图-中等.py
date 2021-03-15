# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c9480213597e45f4807880c763ddd5f0?tpId=117&&tqId=37848&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
请根据二叉树的前序遍历，中序遍历恢复二叉树，并打印出二叉树的右视图

示例1
输入
复制
[1,2,4,5,3],[4,2,5,1,3]
返回值
复制
[1,3,5]
备注:
二叉树每个节点的值在区间[1,10000]内，且保证每个节点的值互不相同。

直接拼贴NC12和NC15即可.
'''
class Solution:
    def solve(self , xianxu , zhongxu ):
        # write code here
        tree = self.reConstructBinaryTree(xianxu, zhongxu)
        levels = self.levelOrder(tree)
        res = []
        for level in levels:
            res.append(level[-1])
        return res

    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        preorder, inorder = pre, tin
        ### if the length of the list is 0:
        if len(preorder) == 0:
            return None
        ### if the length of the list is only 1:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        ### basic logic
        root = TreeNode(preorder[0])
        ##
        mid_index = inorder.index(preorder[0])
        #
        l_in_left = inorder[0:mid_index]
        l_pre_left = preorder[1:len(l_in_left) + 1]
        root.left = self.reConstructBinaryTree(l_pre_left, l_in_left)
        #
        l_in_right = inorder[mid_index + 1:]
        l_pre_right = preorder[len(l_in_left) + 1:]
        root.right = self.reConstructBinaryTree(l_pre_right, l_in_right)
        return root

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