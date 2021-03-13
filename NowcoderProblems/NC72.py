'''
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
比如：    源二叉树
            8
           /  \
          6   10
         / \  / \
        5  7 9 11
        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7  5
示例1
输入
复制
{8,6,10,5,7,9,11}
返回值
复制
{8,10,6,11,9,7,5}

好办. 递归就行了.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTreeFromList(l):
    l_node = []
    for _ in l:
        if _ == "#":
            l_node.append(None)
        else:
            l_node.append(TreeNode(_))
    i = 0
    while i < len(l_node):
        if l_node[i] == None:
            pass
        else:
            if i * 2 + 1 < len(l_node):
                l_node[i].left = l_node[i * 2 + 1]
            if i * 2 + 2 < len(l_node):
                l_node[i].right = l_node[i * 2 + 2]
        i += 1
    return l_node[0]

class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return pRoot
        tmp = pRoot.left
        pRoot.left = self.Mirror(pRoot.right)
        pRoot.right = self.Mirror(tmp)
        return pRoot

tree = buildTreeFromList([8,6,10,5,7,9,11])
mirrorTree = Solution().Mirror(tree)
print()