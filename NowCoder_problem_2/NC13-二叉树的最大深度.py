class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self , root: TreeNode) -> int:
        # write code here
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

'''
描述
求给定二叉树的最大深度，
深度是指树的根节点到任一叶子节点路径上节点的数量。
最大深度是所有叶子节点的深度的最大值。
（注：叶子节点是指没有子节点的节点。）


数据范围：0 \le n \le 1000000≤n≤100000，树上每个节点的val满足 |val| \le 100∣val∣≤100
要求： 空间复杂度 O(1)O(1),时间复杂度 O(n)O(n)
示例1
输入：
{1,2}
复制
返回值：
2
复制
示例2
输入：
{1,2,3,4,#,#,5}
复制
返回值：
3
复制
'''