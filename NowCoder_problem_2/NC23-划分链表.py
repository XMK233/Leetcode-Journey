class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

class Solution:
    def partition(self , head: ListNode, x: int) -> ListNode:
        # write code here
        ## 有一种思路：遍历原来的链表，把大于的挪移到链表的末尾去。
        ## 其实另一种更好做的思路，就是，维护两个链表，一个专门放小于的数，一个放大于的数
        if not head:
            return head

        bigHead, bigTail = None, None
        smallHead, smallTail = None, None
        tgtHead, tgtTail = None, None

        tmpHead = head

        while tmpHead:
            if tmpHead.val < x:
                if smallHead == None:
                    smallHead, smallTail = tmpHead, tmpHead
                    tmpHead = tmpHead.next
                    smallTail.next = None
                else:
                    tmp = tmpHead
                    tmpHead = tmpHead.next
                    smallTail.next = tmp
                    smallTail = smallTail.next
                    smallTail.next = None
            else:
                if bigHead == None:
                    bigHead, bigTail = tmpHead, tmpHead
                    tmpHead = tmpHead.next
                    bigTail.next = None
                else:
                    tmp = tmpHead
                    tmpHead = tmpHead.next
                    bigTail.next = tmp
                    bigTail = bigTail.next
                    bigTail.next = None

        if smallHead == None:
            return bigHead
        else:
            smallTail.next = bigHead
            return smallHead

    def partition1(self, head, x):
        ## 这个方法是抄的。比我的实现更优雅。
        ## 这个哑节点的设计还是巧妙的。
        # 创建两个哑结点
        smallHead = smallTail = ListNode(0)
        largeHead = largeTail = ListNode(0)
        # 遍历链表
        while head:
            # 如果head.val<x,将当前节点插入small中，否则插入large中
            if head.val < x:
                smallTail.next = head
                smallTail = smallTail.next
            else:
                largeTail.next = head
                largeTail = largeTail.next
            head = head.next
        largeTail.next = None
        # 合并两个链表
        smallTail.next = largeHead.next
        return smallHead.next
rst = Solution().partition1(n1, 3)

print("nimabi")

