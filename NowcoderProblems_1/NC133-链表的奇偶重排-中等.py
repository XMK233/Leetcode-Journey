# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/02bf49ea45cd486daa031614f9bd6fc3?tpId=117&&tqId=37845&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个单链表，请设定一个函数，将链表的奇数位节点和偶数位节点分别放在一起，重排后输出。
注意是节点的编号而非节点的数值。

示例1
输入
复制
{1,2,3,4,5,6}
返回值
复制
{1,3,5,2,4,6}
示例2
输入
复制
{1,4,6,3,7}
返回值
复制
{1,6,7,4,3}
说明
奇数节点有1,6,7，偶数节点有4,3。重排后为1,6,7,4,3
备注:
链表长度不大于200000。每个数范围均在int内。

本来非常简单的题, 自己吓自己, 搞得特别复杂, 反倒错了.
参考的方法多简单, 就直接啊, 就把, 啊, 一个链表拆开成两个后首尾相接即可. 多好啊.
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def oddEvenList(self , head ):
        # write code here
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

def buildChainFromList(l):
    nodes = [ListNode(i) for i in l]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

c = buildChainFromList([1,4,6,3,7])
a = Solution().oddEvenList(c)
print()