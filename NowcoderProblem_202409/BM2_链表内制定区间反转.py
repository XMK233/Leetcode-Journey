class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param m int整型
# @param n int整型
# @return ListNode类
#
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        思路是啥呢：每一次遍历到某个应该逆序的节点，就给他放到合适的地方去就好了.
        错误分析：【1】如果m和n分别是第一和最后一个位置呢？本质上就是全链表逆序。
                如果还要采用上中后三截式解决，最好在head前面加一个空头。
                这样上段就是单独一个空头，中段就是要逆序的部分，后段就是None，就不容易错。
        '''

        ## 第一步，确定上半截链条的起止点，确定逆序范围的起止点，确定后半截的开始点。
        ## 第二步，遍历逆序范围的节点，然后按序把每一个节点给它接到后半截的开头。
        ## 第三步，上半截链条的结束点连接到新的后半截的开头，完事儿了。
        ## 链表长度肯定比0要大。然后m可能跟n一样，然后n可能到链表的最后。

        ## 第一种情况，如果m==n，那什么也不用做了。
        if m == n:
            return head

        ## 第二种情况，那就是普通情况。
        ### part_1就是上半截链条：
        new_head = ListNode(-1)
        new_head.next = head
        part_1_start = new_head
        part_1_end = new_head
        for i in range(m - 1):
            part_1_end = part_1_end.next
        ### part_2就是下半截链条：
        part_2_start = part_1_end.next
        part_2_end = part_1_end
        for i in range(n-m+1):
            part_2_end = part_2_end.next
        ### part_3就是最后一截链条：
        part_3_start = part_2_end.next
        ## 然后就可以开始反转了：
        new_part_3_start = part_3_start
        node = part_2_start
        for i in range(n-m+1):
            node_next = node.next
            node.next = new_part_3_start
            new_part_3_start = node
            node = node_next
        part_1_end.next = new_part_3_start

        return part_1_start.next
