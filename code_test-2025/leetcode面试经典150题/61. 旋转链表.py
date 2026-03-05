'''中等
相关标签
premium lock icon
相关企业
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]
 

提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109'''

# Definition for singly-linked list.
# LeetCode 在线环境会提供 ListNode 定义，这里注释仅做参考
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
        # 特殊情况处理：空链表、单节点或不需要移动
        if not head or not head.next or k == 0:
            return head

        # 1. 先遍历一遍链表，得到长度 len，并找到尾节点 tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. k 可能大于链表长度，旋转 len 次等价于不动
        k %= length
        if k == 0:
            return head

        # 3. 把链表连成环：尾节点指向头节点
        tail.next = head

        # 4. 计算新尾节点的位置：它在“从头开始”的第 (length - k - 1) 个位置
        #   新头节点则是新尾节点的 next
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        new_head = new_tail.next

        # 5. 断开环，新尾的 next 置为 None
        new_tail.next = None

        return new_head


if __name__ == "__main__":
    # 简单本地测试工具函数
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

        def __repr__(self):
            return f"{self.val}->{self.next!r}"

    def build_list(vals):
        dummy = ListNode(0)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def to_list(node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    sol = Solution()
    head1 = build_list([1, 2, 3, 4, 5])
    rotated1 = sol.rotateRight(head1, 2)
    print(to_list(rotated1))  # [4, 5, 1, 2, 3]

    head2 = build_list([0, 1, 2])
    rotated2 = sol.rotateRight(head2, 4)
    print(to_list(rotated2))  # [2, 0, 1]
        
