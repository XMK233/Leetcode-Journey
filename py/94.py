# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## https://blog.csdn.net/yangjingjing9/article/details/77054899
## 思路, 我自己能想出来. 总体上来讲还是较为简单的, 注意要使用栈.
## 用栈. 一个节点入栈, 然后不断地把它的左节点入栈. 直到一个节点没有左节点了, 那就pop出来打印, 然后把这个节点的右子放进栈.
## 我借鉴的思想应该是优化了的, 比较简洁.

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.iterative_inorder(root, res)
        print(res)
        return res
    def iterative_inorder(self, root, res):#迭代中序遍历
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res