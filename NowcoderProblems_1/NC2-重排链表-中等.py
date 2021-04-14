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
        # # write code here
        if not head:
            return
        midNode = self.middleNode(head)
        ## section1: 切断链表
        l2 = midNode.next
        midNode.next = None
        ## section2: 逆序l2链表
        l2_rev = self.reverseList(l2)
        ## section3: 合并两个链表l2_rev以及head
        return self.mergeList(head, l2_rev)

    def middleNode(self, node):
        slow = node
        fast = node
        while (fast.next != None and fast.next.next != None): ## 这里判断的是, fast能否一次走两步. 一次走一步都不行, 非得一次走两步才行.
            ## 如果能的话, 就尚未找到中点; 如果不能的话, 那么slow指针指到的地方就是中点.
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
        newL1 = node1
        newL2 = node2
        while newL2 != None: ##这里待会改一下
            tmp = newL1.next
            newL1.next = newL2
            newL1 = newL2
            newL2 = tmp
        return node1

