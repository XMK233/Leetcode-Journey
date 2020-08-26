"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return
        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
## 道理一看就懂，不解释。
## https://blog.csdn.net/fuxuemingzhu/article/details/79559645
## 不知道把所有的节点按层摆出来后，一层一层处理，这种方法跟上述方法比孰优孰劣。