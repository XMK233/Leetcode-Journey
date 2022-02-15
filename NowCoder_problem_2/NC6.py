class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def maxPathSum(self, root):
        # write code here
        self.res = float('-inf')  # 负无穷 这个是一个结果的记录点, 记录的是一棵树的结果. 而dfs函数返回的却是相当于一条链而非一棵树的结果.

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.res = max(self.res, root.val + l + r)
            return max(0, max(l, r) + root.val)

        _ = dfs(root)
        return self.res

class Solution:
    ## 没有理由证明我的实现是错的，但是我的方法确实不够好，太冗余。
    ## 看看人家的Solution1，是不是更完美?
    def maxPathSum(self , root: TreeNode) -> int:
        # write code here
        if root == None:
            return 0

        if root.left != None and root.right != None:
            left_single_chain = self.max_single_chain(root.left)
            right_single_chain = self.max_single_chain(root.right)
            left_max = self.maxPathSum(root.left)
            right_max = self.maxPathSum(root.right)
            return max(
                left_max,
                right_max,
                left_single_chain,
                right_single_chain,
                root.val,
                left_single_chain + root.val,
                right_single_chain + root.val,
                left_single_chain + root.val + right_single_chain
            )
        elif root.left == None and root.right != None:
            right_single_chain = self.max_single_chain(root.right)
            right_max = self.maxPathSum(root.right)
            return max(
                right_max,
                right_single_chain,
                root.val,
                right_single_chain + root.val,
            )
        elif root.left != None and root.right == None:
            left_single_chain = self.max_single_chain(root.left)
            left_max = self.maxPathSum(root.left)
            return max(
                left_max,
                left_single_chain,
                root.val,
                left_single_chain + root.val,
            )
        elif root.left == None and root.right == None:
            return root.val

    def max_single_chain(self, root):
        if not root:
            return 0
        max_side_sum = max(
            self.max_single_chain(root.left),
            self.max_single_chain(root.right)
        )
        return max(root.val, root.val + max_side_sum)

# n1 = TreeNode(-20)
# n2 = TreeNode(8)
# n3 = TreeNode(20)
# n4 = TreeNode(15)
# n5 = TreeNode(6)
# n1.left = n2
# n1.right = n3
# n3.left = n4
# n3.right = n5

# n1 = TreeNode(-2)
# n2 = TreeNode(-3)
# n1.right = n2

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3


s = Solution()
print(s.maxPathSum(n1))
