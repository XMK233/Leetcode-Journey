## 回文链表判断.
## 2021年4月5日 今天刚做过就考, 结果还是没有记住O(1)空间复杂度的解法: 中间把链表破开, 一半反转, 然后对比.
## 不过经过面试官提醒了最优解之后, 也算是一口气做对了.

def isHuiwen(head):
    def reverseChain(node):
        h = None
        cur = node
        pre = node.next
        while pre:
            cur.next = h
            h = cur
            cur = pre
            pre = cur.next
        return cur

    def findMidPoint(node):
        slow, fast = node, node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    mid = findMidPoint(head)
    l1 = head
    l2 = mid.next
    mid.next = None
    l2_rev = reverseChain(l2)
    p1, p2 = l1, l2_rev
    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

from BuildChainFromList import buildChainFromList
chain1 = buildChainFromList([1, 2, 3, 4, 3, 2, 1])
chain2 = buildChainFromList([1, 2, 3, 3, 2, 1])
chain3 = buildChainFromList([1, 2, 3, 3, 2,])
chain4 = buildChainFromList([1, 2, 3, 3, 2, 1, 4])
chain5 = buildChainFromList([1, 2])
print(isHuiwen(chain5))




