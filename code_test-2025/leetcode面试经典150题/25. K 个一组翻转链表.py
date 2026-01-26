'''困难
相关标签
premium lock icon
相关企业
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
示例 2：



输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
 

提示：
链表中的节点数目为 n
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        K个一组翻转链表
        解题思路：迭代法 + 虚拟头节点 + 局部翻转
        时间复杂度：O(n)，其中n是链表长度
        空间复杂度：O(1)，只使用常数额外空间
        """
        # 特殊情况处理：如果k为1，不需要翻转
        if k == 1:
            return head
        
        # 创建虚拟头节点，方便处理翻转头节点的情况
        dummy = ListNode(0, head)
        
        # 计算链表长度，确定需要翻转的组数
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # 初始化前驱节点prev指向虚拟头节点
        prev = dummy
        
        # 计算需要翻转的组数
        groups = length // k
        
        # 进行groups次翻转
        for _ in range(groups):
            # 初始化当前组的第一个节点为prev.next
            group_first = prev.next
            # 初始化当前组的最后一个节点为group_first
            group_last = group_first
            
            # 检查当前组是否有k个节点
            # （实际上由于groups = length // k，这里应该总是有k个节点）
            for __ in range(k - 1):
                if not group_last.next:
                    return dummy.next
                group_last = group_last.next
            
            # 记录下一组的第一个节点
            next_group_first = group_last.next
            
            # 翻转当前组的k个节点
            # 翻转后，group_first变为当前组的最后一个节点
            # group_last变为当前组的第一个节点
            new_group_first, new_group_last = self.reverse_list(group_first, group_last)
            
            # 将翻转后的组连接到链表中
            prev.next = new_group_first
            new_group_last.next = next_group_first
            
            # 更新prev为下一组的前驱节点（即当前组的最后一个节点）
            prev = new_group_last
        
        # 返回新的头节点
        return dummy.next
    
    def reverse_list(self, head: ListNode, tail: ListNode) -> tuple[ListNode, ListNode]:
        """
        翻转指定区间内的链表节点
        参数：
            head: 区间的第一个节点
            tail: 区间的最后一个节点
        返回：
            (new_head, new_tail): 翻转后的头节点和尾节点
        """
        # 初始化前驱节点为None（翻转后tail的next将指向None）
        prev = None
        # 初始化当前节点为head
        current = head
        
        # 翻转链表直到current到达tail的下一个节点
        while prev != tail:
            # 保存下一个节点
            next_node = current.next
            # 翻转指针：当前节点的next指向前驱节点
            current.next = prev
            # 更新前驱节点为当前节点
            prev = current
            # 更新当前节点为下一个节点
            current = next_node
        
        # 翻转后，原来的tail变为头节点，原来的head变为尾节点
        return tail, head

# 辅助函数：创建链表
def create_linked_list(arr):
    if not arr:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# 辅助函数：将链表转换为列表，方便打印
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 示例1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    k1 = 2
    result1 = solution.reverseKGroup(head1, k1)
    print("示例1:")
    print(f"输入：head = [1,2,3,4,5], k = {k1}")
    print(f"输出：{linked_list_to_list(result1)}")
    print(f"预期：[2,1,4,3,5]")
    print()
    
    # 示例2
    head2 = create_linked_list([1, 2, 3, 4, 5])
    k2 = 3
    result2 = solution.reverseKGroup(head2, k2)
    print("示例2:")
    print(f"输入：head = [1,2,3,4,5], k = {k2}")
    print(f"输出：{linked_list_to_list(result2)}")
    print(f"预期：[3,2,1,4,5]")
    print()
    
    # 测试边界情况：k=1
    head3 = create_linked_list([1, 2, 3, 4, 5])
    k3 = 1
    result3 = solution.reverseKGroup(head3, k3)
    print("测试边界情况：k=1")
    print(f"输入：head = [1,2,3,4,5], k = {k3}")
    print(f"输出：{linked_list_to_list(result3)}")
    print(f"预期：[1,2,3,4,5]")
        