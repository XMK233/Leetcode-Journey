'''
[剑指 Offer 26. 树的子结构 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof)

输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false


示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true

限制：

0 <= 节点个数 <= 10000
'''

## 有一个坑，就是如果这些节点的val是会重复的，比如例题里面，值为4的节点有俩。
## 直接就做出来了，没有参考。而且做的还可以。应该能够独立面对这种题目的吧。
'''
解析一下. 就是啊, isSubStructure方法是需要去找一个节点跟待查树的根节点一样,然后在判断后面的树的.
如果当前根节点跟待查根节点不一样, 也可以进行下去, 直到遍历完或者是找到为止. 
而subTreeIsSubStructure不一样, 是不能从当前根节点去找一个跟待查节点一样的节点然后递归的. 如果关键路径上找到不一样的节点, 是会GG的.

所以还真就得按照我的这个实现来做. 没有捷径可以走. 我这个方法估计就是我能想到的极限了. 
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def subTreeIsSubStructure(self, root1, root2):
        ## 两者皆空
        if root1 == root2 == None:
            return True
        ## 两者皆不空
        if root1 != None and root2 != None:
            ## 两个值不等，GG。
            if root1.val != root2.val:
                return False
            else:
                leftPartRst = rightPartRst = True
                ## 右树的子树如果是None，那就不用判断了；若非None，就递归接着判断。
                if root2.left != None:
                    leftPartRst = self.subTreeIsSubStructure(root1.left, root2.left)
                if root2.right != None:
                    rightPartRst = self.subTreeIsSubStructure(root1.right, root2.right)
                return leftPartRst and rightPartRst
        ## 一者为空
        return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A == None:
            return False
        if B == None:
            return False
        ## 假设都不是空节点
        ### 判断两棵原始树的根节点，如果根节点一样，就判断这两颗子树
        ### 就算两颗子树的结果为false，那么因为B.val在A树里面可能多次出现，所以还不能最终返回false；但是如果返回的true，那就可以直接返回true了。
        if A.val == B.val:
            partRst = self.subTreeIsSubStructure(A, B) #self.subTreeIsSubStructure(A.left, B.left) and self.subTreeIsSubStructure(A.right, B.right)
            if partRst == True:
                return True
        ## 然后判断A的左右子树能否包含B树。
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
    ###############################################################################################3

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