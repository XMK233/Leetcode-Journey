class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

## 思路很简单，就是判断两个根节点是不是一样，如果一样的话，那么root1的左子树和root2的右子树应该对称，root1的右子树和root2的左子树应该对称，然后递归即可。
## 很爽吧。