# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/71cef9f8b5564579bf7ed93fbe0b2024?tpId=117&&tqId=37729&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
例如：
给出的链表为1 \to 2\to 3\to 3\to 4\to 4\to51→2→3→3→4→4→5, 返回1\to 2\to51→2→5.
给出的链表为1\to1 \to 1\to 2 \to 31→1→1→2→3, 返回2\to 32→3.



示例1
输入
复制
{1,2,2}
返回值
复制
{1}

只是抄了答案, 还没探索. 不过思路还算是清晰的. 一个难点在于, 如果重复的是头节点那个值, 怎么办?
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
    def deleteDuplicates(self , head ):
        # write code here
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return dummy.next