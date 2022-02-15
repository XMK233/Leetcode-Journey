class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self , root: TreeNode) -> int:
        # write code here
        res, path = [], []
        ## 这是一个回溯算法
        def dfs(node):
            if not node:
                return
            path.append(str(node.val))
            ## 如果遍历到叶子节点：
            if node.left == None and node.right == None:
                res.append(''.join(path))
            ## 递归到左右两个节点：
            dfs(node.left)
            dfs(node.right)
            path.pop(-1)## 回溯的话，是要把最后一个进去的值吐出来的。
            return
        dfs(root)

        s = 0
        for n_str in res:
            s += int(n_str)
        return s

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

print(Solution().sumNumbers(n1))