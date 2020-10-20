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

from help_buildTree import buildTreeFromList
null = None
A = buildTreeFromList([4,2,3,4,5,6,7,8,9])
B = buildTreeFromList([4,8,9])
s = Solution()
print(s.isSubStructure(A, B))

## 有一个坑，就是如果这些节点的val是会重复的，比如例题里面，值为4的节点有俩。
## 直接就做出来了，没有参考。而且做的还可以。应该能够独立面对这种题目的吧。