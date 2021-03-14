# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/650474f313294468a4ded3ce0f7898b9?tpId=117&&tqId=37714&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
判断给定的链表中是否有环。如果有环则返回true，否则返回false。
你能给出空间复杂度的解法么？

快慢指针，一个走一步，一个走两步，如果两者能碰在一起，就有环。如果其中一个变成none，就没有环。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self , head ):
        # write code here
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False