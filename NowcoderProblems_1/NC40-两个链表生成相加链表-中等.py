# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c56f6c70fb3f4849bc56e33ff2a50b6b?tpId=117&&tqId=37814&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。
例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。
示例1
输入
复制
[9,3,7],[6,3]
返回值
复制
{1,0,0,0}
备注:
1 \leq n, m \leq 10^61≤n,m≤10
6

0 \leq a_i, b_i \leq 90≤a
i
​
 ,b
i
​
 ≤9

参考的思路是酱紫的: 反转两个链表后加法, 再把结果链表反转回来即可.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head1 ListNode类
# @param head2 ListNode类
# @return ListNode类
#
class Solution:
    def addInList(self, head1, head2):
        # write code here
        if not head1:
            return head2
        if not head2:
            return head1
        node1, l1 = self.reverse(head1)
        node2, l2 = self.reverse(head2)
        if l1 >= l2:
            head = node = node1
            other = node2
        else:
            head = node = node2
            other = node1
        flag = 0
        while node1 and node2:
            tmp = node1.val + node2.val + flag
            flag = 1 if tmp >= 10 else 0
            node.val = tmp % 10
            node1 = node1.next
            node2 = node2.next
            if node.next:
                node = node.next
        while l1 != l2 and node and flag:
            tmp = node.val + flag
            flag = 1 if tmp >= 10 else 0
            node.val = tmp % 10
            if node.next:
                node = node.next
            else:
                break
        if flag:
            other.next = None
            other.val = 1
            node.next = other
        return self.reverse(head)[0]

    def reverse(self, head):
        if not head:
            return None, 0
        last, cur, nxt, num = None, head, head.next, 0
        while nxt:
            cur.next = last
            last = cur
            cur = nxt
            nxt = nxt.next
            num += 1
        cur.next = last
        return cur, num