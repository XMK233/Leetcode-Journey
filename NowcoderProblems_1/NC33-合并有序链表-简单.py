# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/a479a3f0c4554867b35356e0d57cf03d?tpId=117&&tqId=37735&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
将两个有序的链表合并为一个新链表，要求新的链表是通过拼接两个链表的节点来生成的，且合并后新链表依然有序。

示例1
输入
复制
{1},{2}
返回值
复制
{1,2}
示例2
输入
复制
{2},{1}
返回值
复制
{1,2}

剑指offer 25。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## 二大皆空
        if l1 == l2 == None:
            return l1
        ## 一个为空
        if l1 != None and l2 == None:
            return l1
        if l1 == None and l2 != None:
            return l2
        ## 二者皆不为空
        newHead = None
        if l1.val < l2.val:
            newHead = l1
            laterPartHead = self.mergeTwoLists(l1.next, l2)
        else:
            newHead = l2
            laterPartHead = self.mergeTwoLists(l1, l2.next)
        newHead.next = laterPartHead
        return newHead
