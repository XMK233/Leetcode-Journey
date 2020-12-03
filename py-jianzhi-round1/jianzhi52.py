class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


# 作者：z1m
# 链接：https: // leetcode - cn.com / problems / liang - ge - lian - biao - de - di - yi - ge - gong - gong - jie - dian - lcof / solution / shuang - zhi - zhen - fa - lang - man - xiang - yu - by - ml - zimingm /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 思路：两个指针，node1和node2，分别从headA和headB开始。
# node1遍历一遍后，跳到headB重新开始；node2遍历一遍后，从headA重新开始。一句话，我的路走完了，就走你走过的路，然后我俩皆是如此走，一定会相遇。
## 为什么要走别人走过的路？我不是很能理解。
### 不过这种解法相对来讲还是比较高端的。
# 一个比较一般的解法就是，将两个链表的长度计算出来，然后长的那个链表先遍历一部分，然后两个链表同时遍历，然后遍历到相同节点为止。