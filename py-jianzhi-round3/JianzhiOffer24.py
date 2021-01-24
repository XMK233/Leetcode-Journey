'''
[剑指 Offer 24. 反转链表 - 力扣（LeetCode）](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof)

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

 

限制：

0 <= 节点个数 <= 5000

 

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/
'''


'''
## 普通递归罢了. 也就是把头节点拿下, 然后把后面的反过来, 然后把拿下的头节点连接到后面的反过来的链表的尾端.

可以参考 https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/solution/dong-hua-yan-shi-duo-chong-jie-fa-206-fan-zhuan-li/
我自己的思路跟参考的这个人的递归思路有类似之处. 
不过这个人的思路里面, 他无需返回尾节点就能搞定. 他的代码里面的head.next就相当于我的尾节点. 
所以我只要做一点点改进, 就能够实现他的思路. 
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def helper(self, n):
        if n == None:
            return None, None
        if n != None and n.next == None:
            ## 返回头节点和尾节点
            return n, n
        head = n
        newHead, newTail = self.helper(head.next)
        newTail.next = head
        head.next = None
        return newHead, head

    def reverseList(self, head: ListNode) -> ListNode:
        newHead, newTail = self.helper(head)
        return newHead

# from help_buildTree import buildChain, printChain
# chain = buildChain([1, 2, 3, 4, 5])
# printChain(Solution().reverseList(chain))


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