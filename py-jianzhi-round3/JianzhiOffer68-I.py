'''
[剑指 Offer 68 - I. 二叉搜索树的最近公共祖先 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof)

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]



 

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。


示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。

 

说明:


	所有节点的值都是唯一的。
	p、q 为不同节点且均存在于给定的二叉搜索树中。


注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ## 边界条件
        if root == None:
            return None
        ## 如果有一个点直接就是root, 那么就直接返回root即可啦.
        if root == p or root == q:
            return root
        ## 剩下的情况就是比较复杂的普通情况了.
        ### 情况1: p,q一大一小于root, 分居两侧, 那么root就是共祖.
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        ### 情况2: 都小于
        elif p.val < root.val and q.val < root.val: # (p.val + q.val) < 2 * root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        ### 情况3: 都大于
        elif p.val > root.val and q.val > root.val: # (p.val + q.val) > 2 * root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return None

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