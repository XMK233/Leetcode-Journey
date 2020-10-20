"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

## 中序遍历, 然后暴力连接就好了.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        ## 唯一需要考虑空节点的时候就是root本身就是空节点的时候.
        if root == None:
            return None
        ## 如果root不是所谓空节点. 那么根据我们的逻辑, 此后的所有的root都不会是空节点.
        if root.left == root.right == None:
            root.left = root
            root.right = root
            return root
        elif root.left != None and root.right == None:
            leftHead = self.treeToDoublyList(root.left)
            leftTail = leftHead.left
            leftTail.right = root
            root.left = leftTail
            root.right = leftHead
            leftHead.left = root
            return leftHead
        elif root.left == None and root.right != None:
            rightHead = self.treeToDoublyList(root.right)
            rightTail = rightHead.left
            root.right = rightHead
            rightHead.left = root
            root.left = rightTail
            rightTail.right = root
            return root
        else:
            leftHead = self.treeToDoublyList(root.left)
            leftTail = leftHead.left
            rightHead = self.treeToDoublyList(root.right)
            rightTail = rightHead.left
            leftTail.right = root
            root.left = leftTail
            root.right = rightHead
            rightHead.left = root
            leftHead.left = rightTail
            rightTail.right = leftHead
            return leftHead

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n4.left = n2
n4.right = n5
n2.left = n1
n2.right = n3

s = Solution()
head = s.treeToDoublyList(n4)
## 往右走:
print("going right")
h = head
print(h.val)
h = head.right
while h != head:
    print(h.val)
    h = h.right
## 往左走
print("going left")
h = head
print(h.val)
h = head.left
while h != head:
    print(h.val)
    h = h.left