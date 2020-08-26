# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val) # 中序中根节点的位置，左边即为左子树，右边由子树
        root.left = self.buildTree(preorder[1 : index + 1], inorder[0 : index])
        root.right = self.buildTree(preorder[index + 1 : len(preorder)], inorder[index + 1 : len(inorder)])
        return root
## https://blog.csdn.net/qqxx6661/article/details/75905524
## 道理很好懂，可以多看几遍。