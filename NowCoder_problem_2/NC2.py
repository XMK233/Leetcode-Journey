class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ## 先找到中点，切两半。
    ##　后一半反转。
    ##　前一半跟后一半交叉拼起来就好了。
    def reorderList(self , head):
        # write code here
        if not head: ## TODO: special cases
            return head
        ## find the mid point
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        later_half_head = slow.next
        slow.next = None
        ## reverse the later
        later_half_head = self.reverse_chain(later_half_head)
        ## merge the two parts
        return self.merge_2_chains(head, later_half_head)

    def merge_2_chains(self, head1, head2):
        if not head2: ## 这里没有想到
            return head1

        cur1, pre1 = head1, head1.next
        cur2, pre2 = head2, head2.next
        while True:
            cur1.next = cur2
            cur2.next = pre1

            cur1 = pre1
            if not cur1:
                break
            pre1 = pre1.next

            cur2 = pre2
            if not cur2:
                break
            pre2 = pre2.next
        return head1

    def reverse_chain(self, head):
        if (not head) or (not head.next):
            return head
        cur = head
        nxt = cur.next
        pre = None
        while True:
            cur.next = pre
            pre = cur
            cur = nxt
            if not nxt:
                break
            nxt = cur.next
        return pre

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

def print_chain(head):
    tmp = head
    l = []
    while tmp:
        l.append(tmp.val)
        tmp = tmp.next
    print(l)

s = Solution()
print_chain(s.reorderList(n1))
