# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ## 如果链表的长度太短，那也就没有什么意义了，直接返回head便可。
        if head == None or head.next == None:
            return head
        ## 这么一来，链表的长度至少为2了
        ## 三个点， 都是英雄的指针, 她们是探索的先锋。
        t = None
        m = head
        h = head.next
        while h != None:
            m.next = t
            t = m
            m = h
            h = h.next
            pass
        ## 如果h指到了null，再执行一轮下述操作，便罢了。
        m.next = t
        return m

n = []
for i in range(1, 6):
    _ = ListNode(6 - i)
    if i == 1:
        _.next = None
    else:
        _.next = n[-1]
    n.append(_)

s = Solution()
new_head = s.reverseList(n[-1])
print("finish")

