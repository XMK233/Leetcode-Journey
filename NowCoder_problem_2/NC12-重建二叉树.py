class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self , pre, vin) -> TreeNode:
        # write code here
        if len(pre) == 0:
            return None

        root_val = pre[0]
        root_node = TreeNode(root_val)

        id_in_vin = vin.index(root_val)
        len_left_subTree = id_in_vin

        root_node.left = self.reConstructBinaryTree(pre[1:1+len_left_subTree], vin[0:id_in_vin])
        root_node.right = self.reConstructBinaryTree(pre[1+len_left_subTree:], vin[id_in_vin+1:])

        return root_node

a = Solution().reConstructBinaryTree(
    [1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]
)
print("heheda", a)

'''
描述
给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建出如下图所示。


提示:
1.vin.length == pre.length
2.pre 和 vin 均无重复元素
3.vin出现的元素均出现在 pre里
4.只需要返回根结点，系统会自动输出整颗树做答案对比
数据范围：n \le 2000n≤2000，节点的值 -10000 \le val \le 10000−10000≤val≤10000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
示例1
输入：
[1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6]
复制
返回值：
{1,2,3,4,#,5,6,#,7,#,#,8}
复制
说明：
返回根节点，系统会输出整颗二叉树对比结果，重建结果如题面图示
示例2
输入：
[1],[1]
复制
返回值：
{1}
复制
示例3
输入：
[1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
复制
返回值：
{1,2,5,3,4,6,7}
复制
'''