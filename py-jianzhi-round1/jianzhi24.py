class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def helper(self, n):
        if n == None:
            return None, None
        if n != None and n.next == None:
            ## 返回头节点和尾节点
            return n, n
        head = n
        newHead, newTail = self.helper(head.next)
        newTail.next = head
        head.next = None
        return newHead, head

    def reverseList(self, head: ListNode) -> ListNode:
        newHead, newTail = self.helper(head)
        return newHead

from help_buildTree import buildChain, printChain
chain = buildChain([1, 2, 3, 4, 5])
printChain(Solution().reverseList(chain))

## 普通递归罢了. 也就是把头节点拿下, 然后把后面的反过来, 然后把拿下的头节点连接到后面的反过来的链表的尾端. 