# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/f95dcdafbde44b22a6d741baf71653f6?tpId=117&&tqId=37750&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个链表，删除链表的倒数第 nn 个节点并返回链表的头指针
例如，
给出的链表为: 1\to 2\to 3\to 4\to 51→2→3→4→5, n= 2n=2.
删除了链表的倒数第 nn 个节点之后,链表变为1\to 2\to 3\to 51→2→3→5.

备注：
题目保证 nn 一定是有效的
请给出请给出时间复杂度为\ O(n) O(n) 的算法
示例1
输入
复制
{1,2},2
返回值
复制
{2}

道理很简单, 看答案吧.
'''
class Solution:
    def removeNthFromEnd(self , head , n):
        fast = head
        slow = head
        pre = head
        while n > 0 :
            fast = fast.next
            n = n -1
        while fast != None:
            fast = fast.next
            pre = slow
            slow = slow.next
        if slow != head:
            pre.next = slow.next
        else:
            head = head.next
        return head