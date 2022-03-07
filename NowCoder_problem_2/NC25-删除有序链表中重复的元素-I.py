
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

class Solution:
    def deleteDuplicates(self , head: ListNode) -> ListNode:
        # write code here
        if not head:
            return head
        tmp = head
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                data = tmp.val
                tmp1 = tmp
                while tmp1.val == data:
                    tmp1 = tmp1.next
                tmp.next = tmp1
                tmp = tmp.next
        return head

a = Solution().deleteDuplicates(n1)
print('mina')




'''
描述
删除给出链表中的重复元素（链表中元素从小到大有序），使链表中的所有元素都只出现一次
例如：
给出的链表为1\to1\to21→1→2,返回1 \to 21→2.
给出的链表为1\to1\to 2 \to 3 \to 31→1→2→3→3,返回1\to 2 \to 31→2→3.

数据范围：链表长度满足 0 \le n \le 1000≤n≤100，链表中任意节点的值满足 |val| \le 100∣val∣≤100
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
示例1
输入：
{1,1,2}
复制
返回值：
{1,2}
复制
示例2
输入：
{}
复制
返回值：
{}
复制
'''