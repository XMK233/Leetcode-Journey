# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
## https://blog.csdn.net/aliceyangxi1987/article/details/50720833
## 没什么花活, 非常简单. 但是这个方法, 是我参考的方法中, 没有去计当前是奇还是偶数的.
## 实谓优雅.
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        odd = oddHead = head
        even = evenHead = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead

        return oddHead