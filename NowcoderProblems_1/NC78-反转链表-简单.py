# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=117&&tqId=37777&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
输入一个链表，反转链表后，输出新链表的表头。
示例1
输入
复制
{1,2,3}
返回值
复制
{3,2,1}
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        ## when the chain is empty
        if not pHead:
            return None
        ##
        tmp = None
        next = pHead.next
        while True:
            pHead.next = tmp
            tmp = pHead
            pHead = next
            if pHead == None:
                return tmp
            else:
                next = pHead.next