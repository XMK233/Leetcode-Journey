class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self , num:list):
        if not num:
            return None
        mid_point = len(num) // 2
        root = TreeNode(num[mid_point])
        root.left = self.sortedArrayToBST(num[:mid_point])
        root.right = self.sortedArrayToBST(num[mid_point+1:])
        return root

print(
    Solution().sortedArrayToBST([1])
)

'''
描述
给定一个升序排序的数组，将其转化为平衡二叉搜索树（BST）.

平衡二叉搜索树指树上每个节点 node 都满足左子树中所有节点的的值都小于 node 的值，右子树中所有节点的值都大于 node 的值，并且左右子树的节点数量之差不大于1

数据范围：0 \le n \le 100000≤n≤10000，数组中每个值满足 |val| \le 5000∣val∣≤5000
进阶：空间复杂度 O(n)O(n) ，时间复杂度 O(n)O(n)

例如当输入的升序数组为[-1,0,1,2]时，转化后的平衡二叉搜索树（BST）可以为{1,0,2,-1}，如下图所示：

或为{0,-1,1,#,#,#,2}，如下图所示：

返回任意一种即可。
示例1
输入：
[-1,0,1,2]
复制
返回值：
{1,0,2,-1}
复制
示例2
输入：
[]
复制
返回值：
{}
复制
'''