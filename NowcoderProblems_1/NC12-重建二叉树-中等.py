# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=117&&tqId=37775&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
示例1
输入
复制
[1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
返回值
复制
{1,2,5,3,4,6,7}
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
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