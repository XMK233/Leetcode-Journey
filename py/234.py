class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ## 边界情况
        if head == None:
            return True
        ## 寻找中点
        chain_length_odd = None
        fast = head
        slow = head
        ## 快的先走. 慢的后走.
        while fast != None:
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
            if fast == None:
                break
            slow = slow.next
        ## 反转后半链.
        re_head = self.reverseList(slow.next)
        ## 前半链的末尾指向None.
        slow.next = None
        ## 开始找茬
        h = head
        r_h = re_head
        while h != None and r_h != None:
            if h.val != r_h.val:
                return False
            else:
                h = h.next
                r_h = r_h.next

        return True

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

# n1 = ListNode(1)
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(3)
# n5 = ListNode(2)
# n6 = ListNode(1)
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6
# n6.next = None

# n1 = ListNode(1)
# n1.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n2.next = None

s = Solution()
print(s.isPalindrome(n1))
