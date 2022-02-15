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
    def Print(self , pRoot: TreeNode):
        # write code here
        if not pRoot:
            return []
        res = []
        nodes = [pRoot]
        layers = [0]
        while nodes: ## TODO
            cur_node = nodes.pop(0)
            cur_layer = layers.pop(0)
            if not cur_node:
                continue
            if len(res) < (cur_layer + 1):
                res.append([])
            res[cur_layer].append(cur_node.val)
            nodes.extend([cur_node.left, cur_node.right])
            layers.extend([cur_layer + 1, cur_layer + 1])
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return res

print(
    Solution().Print(n1)
)

'''
描述
给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）

数据范围：0 \le n \le 15000≤n≤1500,树上每个节点的val满足 |val| <= 100∣val∣<=100
要求：空间复杂度：O(n)O(n)，时间复杂度：O(n)O(n)
例如：
给定的二叉树是{1,2,3,#,#,4,5}

该二叉树之字形层序遍历的结果是
[
[1],
[3,2],
[4,5]
]
示例1
输入：
{1,2,3,#,#,4,5}
复制
返回值：
[[1],[3,2],[4,5]]
复制
说明：
如题面解释，第一层是根节点，从左到右打印结果，第二层从右到左，第三层从左到右。
示例2
输入：
{8,6,10,5,7,9,11}
复制
返回值：
[[8],[10,6],[5,7,9,11]]
复制
示例3
输入：
{1,2,3,4,5}
复制
返回值：
[[1],[3,2],[4,5]]
复制
'''