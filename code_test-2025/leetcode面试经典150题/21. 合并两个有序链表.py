'''简单
相关标签
premium lock icon
相关企业
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个升序链表为一个新的升序链表
        解题思路：迭代法 + 虚拟头节点
        时间复杂度：O(m + n)，其中m和n分别是两个链表的长度
        空间复杂度：O(1)，只使用常数额外空间
        """
        # 创建虚拟头节点，方便处理边界情况（如空链表）
        dummy = ListNode(0)
        
        # 初始化一个指针current，用于构建新链表
        current = dummy
        
        # 同时遍历两个链表，比较当前节点的值
        while list1 and list2:
            # 将值较小的节点接到新链表上
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next  # 移动到list1的下一个节点
            else:
                current.next = list2
                list2 = list2.next  # 移动到list2的下一个节点
            
            # 更新current指针到新链表的末尾
            current = current.next
        
        # 处理剩余节点：将非空链表的剩余部分直接接到新链表末尾
        # 如果list1还有剩余节点
        if list1:
            current.next = list1
        # 如果list2还有剩余节点
        if list2:
            current.next = list2
        
        # 返回新链表的头节点（虚拟头节点的下一个节点）
        return dummy.next

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
    list1_1 = create_linked_list([1, 2, 4])
    list1_2 = create_linked_list([1, 3, 4])
    result1 = solution.mergeTwoLists(list1_1, list1_2)
    print("示例1:")
    print(f"输入：l1 = [1,2,4], l2 = [1,3,4]")
    print(f"输出：{linked_list_to_list(result1)}")
    print(f"预期：[1,1,2,3,4,4]")
    print()
    
    # 示例2
    list2_1 = create_linked_list([])
    list2_2 = create_linked_list([])
    result2 = solution.mergeTwoLists(list2_1, list2_2)
    print("示例2:")
    print(f"输入：l1 = [], l2 = []")
    print(f"输出：{linked_list_to_list(result2)}")
    print(f"预期：[]")
    print()
    
    # 示例3
    list3_1 = create_linked_list([])
    list3_2 = create_linked_list([0])
    result3 = solution.mergeTwoLists(list3_1, list3_2)
    print("示例3:")
    print(f"输入：l1 = [], l2 = [0]")
    print(f"输出：{linked_list_to_list(result3)}")
    print(f"预期：[0]")
        