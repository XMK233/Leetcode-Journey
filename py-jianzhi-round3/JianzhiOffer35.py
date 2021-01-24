'''
[剑指 Offer 35. 复杂链表的复制 - 力扣（LeetCode）](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof)

请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]


示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]


示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]


示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。


 

提示：


	-10000 <= Node.val <= 10000
	Node.random 为空（null）或指向链表中的节点。
	节点数目不超过 1000 。


 

注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-pointer/

 
'''
'''
# 作者：z1m
# 链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 这道题的主要思路是DFS.

我自己又盘了一下，感觉这个DFS方法可以这么理解。
相当于把这个链表看作是一棵树的节点。然后next和random分别是左子树和右子树。
用dfs()辅助方法，就可以将左边和右边分别复制，然后分别赋给新节点的左右节点。
是不是很6.，
'''
class Solution:
    def copyRandomList(self, head):
        def dfs(head):
            if not head: return None
            if head in visited:
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        visited = {}
        return dfs(head)

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