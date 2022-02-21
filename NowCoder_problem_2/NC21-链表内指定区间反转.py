class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

class Solution:
    def reverse_chain(self, node):
        if node.next == None:
            return node, node
        r_head, r_tail = self.reverse_chain(node.next)
        r_tail.next = node
        node.next = None
        return r_head, node

    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:

        # write code here
        pre, rev_head, rev_tail, post = head, head, head, head
        i, j = m - 1, n - 1
        while i > 0:
            rev_head = rev_head.next
            pre = pre.next if i != m - 1 else pre
            rev_tail = rev_tail.next
            i -= 1
            j -= 1
        while j > 0:
            rev_tail = rev_tail.next
            j -= 1
        post = rev_tail.next
        rev_tail.next = None
        if pre != rev_head:
            ## cut the chains
            pre.next = None
            ## reverse the chain part:
            new_rev_head, new_rev_tail = self.reverse_chain(rev_head)
            ## connect the chains
            pre.next, new_rev_tail.next = new_rev_head, post
            return head
        else: ## if the reverse start point is just the head node
            new_rev_head, new_rev_tail = self.reverse_chain(rev_head)
            new_rev_tail.next = post
            return new_rev_head



s = Solution().reverseBetween(n1, 1, 2)
print("heheda")

'''
描述
将一个节点数为 size 链表 m 位置到 n 位置之间的区间反转，要求时间复杂度 O(n)O(n)，空间复杂度 O(1)O(1)。
例如：
给出的链表为 1\to 2 \to 3 \to 4 \to 5 \to NULL1→2→3→4→5→NULL, m=2,n=4m=2,n=4,
返回 1\to 4\to 3\to 2\to 5\to NULL1→4→3→2→5→NULL.

数据范围： 链表长度 0 < size \le 10000<size≤1000，0 < m \le n \le size0<m≤n≤size，链表中每个节点的值满足 |val| \le 1000∣val∣≤1000
要求：时间复杂度 O(n)O(n) ，空间复杂度 O(n)O(n)
进阶：时间复杂度 O(n)O(n)，空间复杂度 O(1)O(1)
示例1
输入：
{1,2,3,4,5},2,4
复制
返回值：
{1,4,3,2,5}
复制
示例2
输入：
{5},1,1
复制
返回值：
{5}
'''