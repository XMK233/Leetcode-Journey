# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/6e630519bf86480296d0f1c868d425ad?tpId=117&&tqId=37713&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
对于一个给定的链表，返回环的入口节点，如果没有环，返回null
拓展：
你能给出不利用额外空间的解法么？

这个解析看上去更好: https://blog.nowcoder.net/n/0abeae05e9884baf8655b3f6625b6d4d?f=comment
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def detectCycle(self, head):
        # write code here
        slow = head
        fast = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return
        else: ## 证明有环后, 将慢指针放回到链表头节点, 然后快慢指针都每次走一步,他们相遇的节点必为环入口点. 这是可以用数学推导的.
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow