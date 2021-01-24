'''
[剑指 Offer 36. 二叉搜索树与双向链表 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof)

输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

 

为了让您更好地理解问题，以下面的二叉搜索树为例：

 



 

我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。

 



 

特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。

 

注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

注意：此题对比原题有改动。
'''

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

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()