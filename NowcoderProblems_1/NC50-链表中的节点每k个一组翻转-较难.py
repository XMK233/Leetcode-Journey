# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/b49c3dc907814e9bbfa8437c251b028e?tpId=117&&tqId=37746&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
将给出的链表中的节点每\ k k 个一组翻转，返回翻转后的链表
如果链表中的节点数不是\ k k 的倍数，将最后剩下的节点保持原样
你不能更改节点中的值，只能更改节点本身。
要求空间复杂度 \ O(1) O(1)
例如：
给定的链表是1\to2\to3\to4\to51→2→3→4→5
对于 \ k = 2 k=2, 你应该返回 2\to 1\to 4\to 3\to 52→1→4→3→5
对于 \ k = 3 k=3, 你应该返回 3\to2 \to1 \to 4\to 53→2→1→4→5

示例1
输入
复制
{1,2,3,4,5},2
返回值
复制
{2,1,4,3,5}

我找到一个思路，就是递归法，前k个节点断开成一个新链，反转，然后后面的部分递归再连接到前面一段上。
这个思路少慢差费。垃圾玩意儿。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseChain(self, node):
        h = None
        cur = node
        pre = node.next
        while pre:
            cur.next = h
            h = cur
            cur = pre
            pre = cur.next
        cur.next = h
        return cur

    def reverseKGroup(self , head , k ):
        if not head:
            return head
        # write code here
        p = head
        tmp_t = k
        while p and tmp_t > 1:
            p = p.next
            tmp_t -= 1
        if p == None:
            return head
        elif p != None:
            nextChain = p.next
            ##
            p.next = None
            newP = self.reverseChain(head)
            p1 = newP
            tmp_t1 = k
            while p1 and tmp_t1 > 1:
                p1 = p1.next
                tmp_t1 -= 1
            p1.next = self.reverseKGroup(nextChain, k)
            return newP

from BuildChainFromList import buildChainFromList
tree = buildChainFromList([1,2,3,4,5])
newTree = Solution().reverseKGroup(tree, 2)
while newTree:
    print(newTree.val)
    newTree = newTree.next

