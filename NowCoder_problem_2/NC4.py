class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self , head: ListNode) -> bool:
        if not head:
            return False
        fast, slow = head, head
        ## 快慢指针判断有无环。
        knot_found = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                knot_found = True
                break
        return knot_found