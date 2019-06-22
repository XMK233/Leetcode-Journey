'''

141. Linked List Cycle
Easy

1315

108

Favorite

Share
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False

        h = head
        r = head
        while True:
            h = h.next
            if r.next != None:
                r = r.next.next
            else:
                return False
            ####
            if h == None or r == None:
                return False
            if h == r and h != None:
                return True

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b
s = Solution()
print(s.hasCycle(a))

