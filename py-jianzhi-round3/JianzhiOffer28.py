'''
[剑指 Offer 28. 对称的二叉树 - 力扣（LeetCode）](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof)

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true


示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false

 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
## 思路很简单，就是判断两个根节点是不是一样，如果一样的话，那么root1的左子树和root2的右子树应该对称，root1的右子树和root2的左子树应该对称，然后递归即可。
## 很爽吧。
'''

class Solution:
    def twoSubTreesAreSymmetric(self, root1, root2):
        ## 二大皆空
        if root1 == root2 == None:
            return True
        ## 一者为空
        if root1 == None and root2 != None or root1 != None and root2 == None:
            return False
        ## 二大皆不空且二者值不同
        if root1.val != root2.val:
            return False
        ## 二大皆不空且二者值相同，那就要递归了
        return self.twoSubTreesAreSymmetric(root1.left, root2.right) and self.twoSubTreesAreSymmetric(root1.right, root2.left)


    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        ##
        return self.twoSubTreesAreSymmetric(root.left, root.right)
##---------------------------------------------------------------------------
def buildTreeFromList(listOfNums):
    ##
    listOfNodes = []
    for n in listOfNums:
        if n != None:
            listOfNodes.append(TreeNode(n))
        else:
            listOfNodes.append(None)
    ##
    for i, n in enumerate(listOfNodes):
        if n == None:
            continue
        if 2 * i + 1 >= len(listOfNodes):
            break
        n.left = listOfNodes[2 * i + 1]
        if 2 * i + 2 >= len(listOfNodes):
            break
        n.right = listOfNodes[2 * i + 2]
    return listOfNodes[0]

null = None
treeRoot = buildTreeFromList([1,2,3])
s = Solution()
print(s.isSymmetric(treeRoot))

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