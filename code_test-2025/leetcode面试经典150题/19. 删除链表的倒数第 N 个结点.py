'''中等
相关标签
premium lock icon
相关企业
提示
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

示例 1：


输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

进阶：你能尝试使用一趟扫描实现吗？'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        删除链表的倒数第n个结点
        解题思路：双指针（快慢指针）技术
        时间复杂度：O(n)，其中n是链表长度
        空间复杂度：O(1)
        """
        # 创建虚拟头节点，方便处理删除头节点的情况
        dummy = ListNode(0, head)
        
        # 初始化快慢指针，都指向虚拟头节点
        fast = slow = dummy
        
        # 1. 先让fast指针向前移动n+1步
        # 这样fast和slow之间就间隔了n个节点
        for _ in range(n + 1):
            fast = fast.next
        
        # 2. 同时移动fast和slow指针，直到fast到达链表末尾
        # 此时slow指针的下一个节点就是要删除的倒数第n个节点
        while fast:
            fast = fast.next
            slow = slow.next
        
        # 3. 执行删除操作
        slow.next = slow.next.next
        
        # 4. 返回新的头节点（注意不是dummy，而是dummy.next）
        return dummy.next

# 辅助函数：创建链表
def create_linked_list(arr):
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
    n1 = 2
    result1 = solution.removeNthFromEnd(head1, n1)
    print("示例1:")
    print(f"输入：head = [1,2,3,4,5], n = {n1}")
    print(f"输出：{linked_list_to_list(result1)}")
    print(f"预期：[1,2,3,5]")
    print()
    
    # 示例2
    head2 = create_linked_list([1])
    n2 = 1
    result2 = solution.removeNthFromEnd(head2, n2)
    print("示例2:")
    print(f"输入：head = [1], n = {n2}")
    print(f"输出：{linked_list_to_list(result2)}")
    print(f"预期：[]")
    print()
    
    # 示例3
    head3 = create_linked_list([1, 2])
    n3 = 1
    result3 = solution.removeNthFromEnd(head3, n3)
    print("示例3:")
    print(f"输入：head = [1,2], n = {n3}")
    print(f"输出：{linked_list_to_list(result3)}")
    print(f"预期：[1]")
        