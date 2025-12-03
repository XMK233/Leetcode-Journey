#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
82. 删除排序链表中的重复元素 II
中等

给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。
返回 已排序的链表 。

示例:
输入: head = [1,2,3,3,4,4,5]
输出: [1,2,5]

输入: head = [1,1,1,2,3]
输出: [2,3]
"""

class ListNode:
    """链表节点定义"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """用于打印链表"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        删除排序链表中的重复元素 II
        
        算法思路:
        1. 使用哑节点(dummy)作为新链表的头节点，简化边界条件处理
        2. 使用prev指针指向当前已处理链表的最后一个节点
        3. 使用current指针遍历原链表
        4. 当发现重复元素时，跳过所有重复节点
        5. 当元素不重复时，将节点添加到结果链表中
        
        时间复杂度: O(n) - 只需遍历一次链表
        空间复杂度: O(1) - 只使用了常数个额外变量
        """
        # 创建哑节点，简化边界条件处理
        dummy = ListNode(0)
        dummy.next = head
        
        # prev指向当前已处理链表的最后一个节点
        prev = dummy
        # current用于遍历原链表
        current = head
        
        while current:
            # 检查当前节点是否有重复
            has_duplicate = False
            
            # 跳过所有重复的节点
            while current.next and current.val == current.next.val:
                current = current.next
                has_duplicate = True
            
            if has_duplicate:
                # 如果有重复，跳过所有重复节点
                prev.next = current.next
            else:
                # 如果没有重复，将当前节点加入结果链表
                prev = current
            
            # 移动到下一个节点
            current = current.next
        
        return dummy.next

def create_linked_list(values):
    """从列表创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例1
    print("测试用例1:")
    head1 = create_linked_list([1, 2, 3, 3, 4, 4, 5])
    print(f"输入: {head1}")
    result1 = solution.deleteDuplicates(head1)
    print(f"输出: {result1}")
    print("预期: 1 -> 2 -> 5")
    print()
    
    # 测试用例2
    print("测试用例2:")
    head2 = create_linked_list([1, 1, 1, 2, 3])
    print(f"输入: {head2}")
    result2 = solution.deleteDuplicates(head2)
    print(f"输出: {result2}")
    print("预期: 2 -> 3")
    print()
    
    # 测试用例3 - 空链表
    print("测试用例3:")
    head3 = create_linked_list([])
    print(f"输入: {head3}")
    result3 = solution.deleteDuplicates(head3)
    print(f"输出: {result3}")
    print("预期: None")
    print()
    
    # 测试用例4 - 所有元素都重复
    print("测试用例4:")
    head4 = create_linked_list([1, 1, 2, 2, 3, 3])
    print(f"输入: {head4}")
    result4 = solution.deleteDuplicates(head4)
    print(f"输出: {result4}")
    print("预期: None")
    print()
    
    # 测试用例5 - 没有重复元素
    print("测试用例5:")
    head5 = create_linked_list([1, 2, 3, 4, 5])
    print(f"输入: {head5}")
    result5 = solution.deleteDuplicates(head5)
    print(f"输出: {result5}")
    print("预期: 1 -> 2 -> 3 -> 4 -> 5")

if __name__ == "__main__":
    test_solution()