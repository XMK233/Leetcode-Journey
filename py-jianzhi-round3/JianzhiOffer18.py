'''
[剑指 Offer 18. 删除链表的节点 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof)

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.


 

说明：


	题目保证链表中节点的值互不相同
	若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

'''
'''
两个指针, 一前一后, 往后遍历, 然后查找即可. 
需要盯住当前遍历指针cur的父节点, 所以咱还需要一个pre. 
'''
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        pre, cur = head, head.next
        ## 只要current非空, 不等于目标值, 就一直重复找下去.
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        ## 如果从循环中退出, 要么是cur等于None了(a.k.a. 找不到要删的值), 要么是cur==目标值了
        ## 如果是第二种情况, 直接删掉就好了. 此时是不会出任何问题的.
        if cur: pre.next = cur.next
        return head

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/mian-shi-ti-18-shan-chu-lian-biao-de-jie-dian-sh-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 这个就没什么好说的了，直接俩指针盯住就好了。非常简单。

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