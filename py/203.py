'''
203. Remove Linked List Elements
Easy

851

51

Favorite

Share
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
Accepted
229,730
Submissions
639,930
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while True:
            if head == None:
                return head
            else:
                if head.val == val:
                    head = head.next
                else:
                    break
        h = head
        while h != None:
            if h == None:
                return head
            elif h.val == val:
                h = h.next
            else:
                if h.next == None:
                    return head
                else:
                    if h.next.val == val:
                        h.next = h.next.next
                    else:
                        h = h.next
        return head

head = ListNode(1)
a = ListNode(2)
b = ListNode(6)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
h = head

while h != None:
    print(h.val)
    h = h.next

print()

s = Solution()
s.removeElements(head, 6)
h = head
while h != None:
    print(h.val)
    h = h.next