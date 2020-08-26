# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        cur = root
        q = collections.deque([cur])
        count = len(q)
        while q:
            tmplevel = []
            while count:
                cur = q.popleft()
                tmplevel.append(cur.val)
                count -= 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(tmplevel)
            count = len(q)
        return ans
## https://xingxingpark.com/Leetcode-102-Binary-Tree-Level-Order-Traversal/
## 我自己采用的思路就是那本最优解书作者介绍的那种。