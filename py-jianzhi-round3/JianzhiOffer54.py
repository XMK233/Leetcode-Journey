'''
[剑指 Offer 54. 二叉搜索树的第k大节点 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof)

给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''

class Solution:
    def kthLargest(self, root, k):
        def dfs(root):
            if not root: return
            ## go to right branch:
            dfs(root.right)
            if self.k == 0: return
            ## see root itself
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            ## go to left branch
            dfs(root.left)
        ## the k is actually stored in a global variable
        self.k = k
        dfs(root)
        return self.res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 相当于用一个全局变量self.k来存储这个k. k是什么呢? 就是第k大的数嘛.
## 然后就从最大的数开始遍历, 遍历一个, k就减少一个, 直到0, 就说明已经找到第k大的数了.
## 这时直接返回就好, 早停, 不要再往下遍历了.

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