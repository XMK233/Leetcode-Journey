class Solution:
    def partition(self , head: ListNode, x: int) -> ListNode:
        # write code here
        ## 有一种思路：遍历原来的链表，把大于的挪移到链表的末尾去。
        return head