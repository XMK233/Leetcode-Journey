class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

n1 = TreeNode(-20)
n2 = TreeNode(8)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(6)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

class Solution:
    def levelOrder(self , root: TreeNode):
        # write code here
        # write code here
        if not root:
            return []
        res = []
        nodes = [root]
        layers = [0]
        while nodes:  ## TODO
            cur_node = nodes.pop(0)
            cur_layer = layers.pop(0)
            if not cur_node:
                continue
            if len(res) < (cur_layer + 1):
                res.append([])
            res[cur_layer].append(cur_node.val)
            nodes.extend([cur_node.left, cur_node.right])
            layers.extend([cur_layer + 1, cur_layer + 1])
        return res
'''
描述
给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
例如：
给定的二叉树是{3,9,20,#,#,15,7},

该二叉树层序遍历的结果是
[
[3],
[9,20],
[15,7]

]


提示:
0 <= 二叉树的结点数 <= 1500


示例1
输入：
{1,2}
复制
返回值：
[[1],[2]]
复制
示例2
输入：
{1,2,3,4,#,#,5}
复制
返回值：
[[1],[2,3],[4,5]]
复制

'''