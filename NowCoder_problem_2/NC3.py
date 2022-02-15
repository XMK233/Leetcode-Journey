class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        fast, slow = pHead, pHead
        ## 快慢指针判断有无环。
        knot_found = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                knot_found = True
                break
        ## 如果没有环，好办。
        if not knot_found:
            return None
        ## 如果有，就因垂丝汀了。
        ## 如果有环，那么一个点放到链表头pHead，另一个放在相遇点，然后它俩同时行进，那么他俩碰到的点就是结点。
        ## 这个是可以用数学推导出来的。
        ## 不信看这个 https://blog.nowcoder.net/n/0abeae05e9884baf8655b3f6625b6d4d?f=comment
        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n10 = ListNode(10)
n11 = ListNode(11)
n12 = ListNode(12)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n11
n11.next = n12
n12.next = n9

def print_chain(head):
    tmp = head
    l = []
    while tmp:
        l.append(tmp.val)
        tmp = tmp.next
    print(l)

s = Solution()
print_chain(s.EntryNodeOfLoop(n1))
