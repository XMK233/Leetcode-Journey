# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/b58434e200a648c589ca2063f1faf58c?tpId=117&&tqId=37726&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
将一个链表\ m m 位置到\ n n 位置之间的区间反转，要求时间复杂度 ，空间复杂度 。
例如：
给出的链表为 1\to 2 \to 3 \to 4 \to 5 \to NULL1→2→3→4→5→NULL, ，,
返回 1\to 4\to 3\to 2\to 5\to NULL1→4→3→2→5→NULL.
注意：
给出的 满足以下条件：
1 \leq m \leq n \leq 链表长度1≤m≤n≤链表长度
示例1
输入
复制
{1,2,3,4,5},2,4
返回值
复制
{1,4,3,2,5}

普通的实现. 不过难度在于边界条件的判断和编码能力.
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head, m, n):
        # write code here
        if not head or not head.next or m == n:
            return head

        prev_node = None
        cur_node = head
        while m > 1:
            prev_node = cur_node
            cur_node = cur_node.next
            m -= 1
            n -= 1

        mid_node, tail_node = prev_node, cur_node
        while n:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            n -= 1

        if mid_node:
            mid_node.next = prev_node
        else:
            head = prev_node

        tail_node.next = cur_node

        return head