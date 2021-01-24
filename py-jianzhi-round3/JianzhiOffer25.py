'''
[剑指 Offer 25. 合并两个排序的链表 - 力扣（LeetCode）](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof)

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ## 二大皆空
        if l1 == l2 == None:
            return l1
        ## 一个为空
        if l1 != None and l2 == None:
            return l1
        if l1 == None and l2 != None:
            return l2
        ## 二者皆不为空
        newHead = None
        if l1.val < l2.val:
            newHead = l1
            laterPartHead = self.mergeTwoLists(l1.next, l2)
        else:
            newHead = l2
            laterPartHead = self.mergeTwoLists(l1, l2.next)
        newHead.next = laterPartHead
        return newHead

# from help_buildTree import buildChain, printChain
# chain1 = buildChain([1,2,4])
# chain2 = buildChain([1,3,4])
# s = Solution()
# printChain(s.mergeTwoLists(chain1, chain2))

## 递归的思想，非常简单。


##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()