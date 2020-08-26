# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ## 归并排序
    def sortList(self, head: ListNode) -> ListNode:
        ## 如果链表长度只有1或者是0, 那就没必要排序了.
        if head == None or head.next == None:
            return head
        ## 否则就正常弄.
        ### 先剖开一半. 用快慢机.
        fast = head
        slow = head
        slow_before = None
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow_before == None:
                slow_before = head
            else:
                slow_before = slow_before.next
        ### 跳出循环的时候, slow就是中间点咯. 此时要截断链表.
        slow_before.next = None
        ### 考虑一般的情况, 也就是链表比较长的时候, 需要递归
        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        cur1 = head1
        cur2 = head2
        new_head = None
        new_tail = None
        ### 合并链表
        while cur1 != None and cur2 != None:
            ## 保证cur1总是小的那个, cur2总是大的那个.
            if cur1.val >= cur2.val:
                tmp = cur1
                cur1 = cur2
                cur2 = tmp
            ## 初始化new_head, 然后就不轻动了.
            if new_head == None:
                new_head = cur1
                # new_tail = cur1
            ## 然后就是要调节cur什么的了.
            if new_tail == None:
                new_tail = cur1
            else:
                new_tail.next = cur1
                new_tail = new_tail.next
            cur1 = cur1.next
            new_tail.next = None
        ### 如果有一个链表没有遍历完, 就全部接上去.
        if cur1 == None and cur2 != None:
            new_tail.next = cur2
        elif cur1 != None and cur2 == None:
            new_tail.next = cur1
        else:
            pass
        return new_head

##########################

node_m1 = ListNode(-1)
node_5 = ListNode(5)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_0 = ListNode(0)
node_m1.next = node_5
node_5.next = node_3
node_3.next = node_4
# node_4.next = node_0

## 测试样例: 长度为0, 1, 偶数, 奇数的链表. 

s = Solution()
head = s.sortList(node_m1)
i = head
while i != None:
    print(i.val)
    i = i.next