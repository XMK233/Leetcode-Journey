class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


class Solution:
    def deleteDuplicates(self, head):
        '''
        这个方法是抄来的。
        这里有一个dummy node的使用。可以借鉴。
        :param head:
        :return:
        '''
        # 如果链表为空，直接返回
        if not head:
            return head
        # 创建一个哨兵节点
        dummy = ListNode(0)
        dummy.next = head

        # 开始时，将cur指向哨兵节点
        cur = dummy
        while cur.next and cur.next.next:
            # 如果cur.next.val和cur.next.next.val相同，删除重复元素
            if cur.next.val == cur.next.next.val:
                data = cur.next.val
                while cur.next and cur.next.val == data:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next




'''
描述
给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
例如：
给出的链表为1 \to 2\to 3\to 3\to 4\to 4\to51→2→3→3→4→4→5, 返回1\to 2\to51→2→5.
给出的链表为1\to1 \to 1\to 2 \to 31→1→1→2→3, 返回2\to 32→3.

数据范围：链表长度 0 \le n \le 100000≤n≤10000，链表中的值满足 |val| \le 1000∣val∣≤1000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
示例1
输入：
{1,2,2}
复制
返回值：
{1}
复制
示例2
输入：
{}
复制
返回值：
{}
复制
'''