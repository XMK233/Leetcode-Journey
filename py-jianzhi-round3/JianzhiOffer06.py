'''
[剑指 Offer 06. 从尾到头打印链表 - 力扣（LeetCode）](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof)

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]

 

限制：

0 <= 链表长度 <= 10000
'''
'''
//作者：jyd
//链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

/*
* 当然可以用递归, 然后得到后面的倒序结果, 然后再把当前的节点的值放到之前得到的倒序结果的后面.
* 不过, 既然这题是简单题, 那为什么不用栈来倒序呢? 呵呵哒.
* */
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode):
        stack = []
        revStack = []
        p = head
        while p != None:
            stack.append(p.val)
            p = p.next
        ## 原理是用栈来倒序.
        while len(stack) != 0:
            revStack.append(stack.pop(-1))
        return revStack

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