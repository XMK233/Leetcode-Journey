# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/3d281dc0b3704347846a110bf561ef6b?tpId=117&&tqId=37712&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
将给定的单链表\ L L： L_0→L_1→…→L_{n-1}→L_ nL
0
​
 →L
1
​
 →…→L
n−1
​
 →L
n
​

重新排序为：L_0→L_n →L_1→L_{n-1}→L_2→L_{n-2}→…L
0
​
 →L
n
​
 →L
1
​
 →L
n−1
​
 →L
2
​
 →L
n−2
​
 →…
要求使用原地算法，不能改变节点内部的值，需要对实际的节点进行交换。
例如：
对于给定的单链表{10,20,30,40}，将其重新排序为{10,40,20,30}.

首先，先找到链表中点。然后把后半部分倒序。再与前半部分拉链式合并起来就好了。
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param head ListNode类
# @return void
#
class Solution:
    def reorderList(self, head):
        # write code here
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, node):
        slow = node
        fast = node
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, node):
        pre = None
        cur = node
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def mergeList(self, node1, node2):
        newL1 = None
        newL2 = None
        while (newL1 != None and newL2 != None):
            next1 = node1.next
            next2 = node2.next
            node1.next = node2
            node2.next = next1
            node1 = next1
            node2 = next2
        return