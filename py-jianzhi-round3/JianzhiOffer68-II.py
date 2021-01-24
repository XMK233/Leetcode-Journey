'''
[剑指 Offer 68 - II. 二叉树的最近公共祖先 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof)

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。


示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。


 

说明:


	所有节点的值都是唯一的。
	p、q 为不同节点且均存在于给定的二叉树中。


注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):  # 判断是否找到
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # 左右深度递归
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:  # 两个节点都找到
            return root
        else:
            return left or right  # 找到其中一个

        return None  # 都没找到（加不加都行，加上严谨点）

#  https://blog.csdn.net/XX_123_1_RJ/article/details/82253978
## 递归里面最基本的情况是什么呢? 就是判断当前节点是不是目标节点或者是空节点.
## 如果是目标节点, 就说明, 在这棵子树里面, 有我要找的点.
## 然后其实就相对比较好理解了.

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