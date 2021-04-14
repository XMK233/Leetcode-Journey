# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/65cfde9e5b9b4cf2b6bafa5f3ef33fa6?tpId=117&&tqId=37747&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

参考思路:
这道题目最容易想到的做法是，使用【合并两个有序链表】中的方法，融合前两个链表，将下一个链表与当前结果融合，遍历列表中的每个链表，不断循环下去。
但是这种方法时间复杂度很高，我们考虑用二分法把列表进行中间拆分，将列表都拆成长度相等的两个列表，然后融合每个小列表中的链表即可。
这样就可以将K级别的融合计算量转换为log(K)级别。

所以参考做法是一个典型的分治解法.
就跟用递归来计算平方的原理一样, 属于分治.
这里是将K个链表的合并分治为两个链表的合并罢了.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        if len(lists) <= 2:
            return self.mergeTwoLists(lists)

        def splitLists(lists):
            idx = len(lists) // 2
            return lists[:idx], lists[idx:]

        a, b = splitLists(lists)
        a_merge = self.mergeKLists(a)
        b_merge = self.mergeKLists(b)
        return self.mergeTwoLists([a_merge, b_merge])

    def mergeTwoLists(self, lists):
        if not lists: return None
        if len(lists) == 1: return lists[0]
        head1, head2 = lists
        cursor = dump = ListNode(0) ## 这里是新建了一个船新的临时节点dump. 以此节点为头哦.
        while head1 and head2:
            if head1.val < head2.val:
                cursor.next = head1
                head1 = head1.next
            else:
                cursor.next = head2
                head2 = head2.next
            cursor = cursor.next
        cursor.next = head1 if head1 else head2
        return dump.next ## 真正返回的时候, 是返回dump此节点的下一个节点, 也就是真正的头节点.