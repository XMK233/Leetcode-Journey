'''
[剑指 Offer 07. 重建二叉树 - 力扣（LeetCode）](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof)

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

 

限制：

0 <= 节点个数 <= 5000

 

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''
'''
没参考, 就很单纯的解它. 利用前序和中序结果, 判断数组的哪一段是左子树, 哪一段是右子树, 然后左右分别递归即可. 
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
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
        root.left = self.buildTree(l_pre_left, l_in_left)
        #
        l_in_right = inorder[mid_index + 1:]
        l_pre_right = preorder[len(l_in_left) + 1:]
        root.right = self.buildTree(l_pre_right, l_in_right)
        return root
