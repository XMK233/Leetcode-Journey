# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/886370fe658f41b498d40fb34ae76ff9?tpId=117&&tqId=37766&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。
示例1
输入
复制
{1,2,3,4,5},1
返回值
复制
{5}

思路很简单。快慢节点即可。

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead , k ):
        ## 如果pHead本身就是空节点，直接GG
        if not pHead:
            return pHead
        head, leading = pHead, pHead
        ## 贯彻落实思路：快节点leading先走若干步，等到leading走到了空节点，那么慢节点head也就走到了倒数第k个节点。
        for _ in range(k):
            if leading != None: ## 这个if判断的是乜？比如链表本身长度为5，但是你要倒数第六个节点，那就直接返回None吧，查无此点。
                leading = leading.next
            else:
                return None
        while leading != None: ## 然后就是正常的快满节点过程。
            head = head.next
            leading = leading.next
        return head
