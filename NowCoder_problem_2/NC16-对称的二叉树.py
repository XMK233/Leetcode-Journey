class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        def isMirrorTree(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 != None and root2 == None:
                return False
            elif root1 == None and root2 != None:
                return False
            elif root1.val != root2.val:
                return False
            return isMirrorTree(root1.left, root2.right) and isMirrorTree(root1.right, root2.left)
        if not pRoot:
            return True
        return isMirrorTree(pRoot.left, pRoot.right)

'''
描述
给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）
例如：                                 下面这棵二叉树是对称的

下面这棵二叉树不对称。

数据范围：节点数满足 0 \le n \le 10000≤n≤1000，节点上的值满足 |val| \le 1000∣val∣≤1000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
备注：
你可以用递归和迭代两种方法解决这个问题
示例1
输入：
{1,2,2,3,4,4,3}
复制
返回值：
true
复制
示例2
输入：
{8,6,9,5,7,7,5}
复制
返回值：
false
复制

'''