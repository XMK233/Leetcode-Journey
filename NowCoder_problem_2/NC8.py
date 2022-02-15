class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# n1 = TreeNode(10)
# n2 = TreeNode(5)
# n3 = TreeNode(12)
# n4 = TreeNode(4)
# n5 = TreeNode(7)
# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5

# n1 = TreeNode(-2)
# n2 = TreeNode(-3)
# n1.right = n2

n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(4)
n1.left = n2
n1.right = n3

class Solution:
    def FindPath(self , root: TreeNode, target: int):
        # write code here
        res, path = [], []

        if not TreeNode:
            return res

        def dfs(node, val):
            if not node:
                return

            path.append(node.val)
            val -= node.val

            if node.left == None and node.right == None and val == 0:
                res.append(path[:])

            dfs(node.left, val)
            dfs(node.right, val)

            path.pop(-1)

        dfs(root, target)

        return res

print(
    Solution().FindPath(n1, 7)
)