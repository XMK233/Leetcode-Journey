# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):  # 判断是否找到
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # 左右深度递归
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:  # 两个节点都找到
            return root
        else:
            return left or right  # 找到其中一个

        return None  # 都没找到（加不加都行，加上严谨点）

#  https://blog.csdn.net/XX_123_1_RJ/article/details/82253978
## 递归里面最基本的情况是什么呢? 就是判断当前节点是不是目标节点或者是空节点.
## 如果是目标节点, 就说明, 在这棵子树里面, 有我要找的点.
## 然后其实就相对比较好理解了.