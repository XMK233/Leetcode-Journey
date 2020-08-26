# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



## 最优解146页。
### 双端队列，有的时候从头部往里压入，有的时候从尾部压入。
### 有的时候先压入左节点再压入右节点；有的时候反之。
## 代码直接抄了：https://www.cnblogs.com/loadofleaf/p/5502296.html
class Solution(object):
    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1: res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0,root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.preorder(root, 0, res)
        print (res)
        return res