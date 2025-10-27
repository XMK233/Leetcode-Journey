# 101. 对称二叉树
# 简单

from typing import Optional
from collections import deque

# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        检查二叉树是否是轴对称的
        
        思路解析（递归方法）：
        1. 一个树是对称的，当且仅当它的左子树和右子树是镜像对称的
        2. 两个树是镜像对称需要满足：
           - 它们的根节点值相同
           - 第一个树的左子树和第二个树的右子树镜像对称
           - 第一个树的右子树和第二个树的左子树镜像对称
        3. 使用辅助函数isMirror来判断两个子树是否镜像对称
        
        参数:
            root: Optional[TreeNode] - 二叉树的根节点
        
        返回:
            bool - 二叉树是否是轴对称的
        """
        # 如果树为空，则它是对称的
        if not root:
            return True
        
        # 检查左子树和右子树是否镜像对称
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """
        辅助函数：检查两个子树是否镜像对称
        
        参数:
            left: Optional[TreeNode] - 第一个子树的根节点
            right: Optional[TreeNode] - 第二个子树的根节点
        
        返回:
            bool - 两个子树是否镜像对称
        """
        # 如果两个子树都为空，则它们是镜像对称的
        if not left and not right:
            return True
        
        # 如果只有一个子树为空，则它们不是镜像对称的
        if not left or not right:
            return False
        
        # 两个子树都不为空，需要满足：
        # 1. 它们的根节点值相同
        # 2. 第一个树的左子树和第二个树的右子树镜像对称
        # 3. 第一个树的右子树和第二个树的左子树镜像对称
        return (left.val == right.val and
                self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))
    
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """
        使用迭代方法检查二叉树是否是轴对称的
        
        思路解析（迭代方法）：
        1. 使用队列来存储需要比较的节点对
        2. 初始时将根节点的左右子节点加入队列
        3. 每次从队列中取出两个节点进行比较：
           - 如果两个节点都为空，继续比较下一对
           - 如果只有一个节点为空，返回False
           - 如果两个节点的值不相同，返回False
           - 如果两个节点的值相同，将它们的子节点按照镜像的方式加入队列
        4. 如果队列为空，则说明所有节点对都比较完成且是对称的，返回True
        
        参数:
            root: Optional[TreeNode] - 二叉树的根节点
        
        返回:
            bool - 二叉树是否是轴对称的
        """
        # 如果树为空，则它是对称的
        if not root:
            return True
        
        # 使用队列存储需要比较的节点对
        queue = deque([(root.left, root.right)])
        
        while queue:
            # 取出队列中的两个节点
            left, right = queue.popleft()
            
            # 如果两个节点都为空，继续比较下一对
            if not left and not right:
                continue
            
            # 如果只有一个节点为空，或者两个节点的值不相同，返回False
            if not left or not right or left.val != right.val:
                return False
            
            # 将子节点按照镜像的方式加入队列
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        
        # 所有节点对都比较完成，且没有发现不对称的情况
        return True

# 测试样例
if __name__ == "__main__":
    solution = Solution()
    
    # 辅助函数：根据列表构建二叉树
    def buildTree(nodes):
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1
        while queue and i < len(nodes):
            node = queue.popleft()
            # 左子节点
            if i < len(nodes) and nodes[i] is not None:
                node.left = TreeNode(nodes[i])
                queue.append(node.left)
            i += 1
            # 右子节点
            if i < len(nodes) and nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.append(node.right)
            i += 1
        return root
    
    # 测试用例1: 对称二叉树
    # 树结构: [1,2,2,3,4,4,3]
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    tree1 = buildTree([1, 2, 2, 3, 4, 4, 3])
    print(f"测试用例1 (递归方法): {solution.isSymmetric(tree1)}")  # 应该输出True
    print(f"测试用例1 (迭代方法): {solution.isSymmetricIterative(tree1)}")  # 应该输出True
    
    # 测试用例2: 非对称二叉树
    # 树结构: [1,2,2,None,3,None,3]
    #     1
    #    / \
    #   2   2
    #    \   \
    #     3   3
    tree2 = buildTree([1, 2, 2, None, 3, None, 3])
    print(f"测试用例2 (递归方法): {solution.isSymmetric(tree2)}")  # 应该输出False
    print(f"测试用例2 (迭代方法): {solution.isSymmetricIterative(tree2)}")  # 应该输出False
    
    # 测试用例3: 空树
    tree3 = buildTree([])
    print(f"测试用例3 (递归方法): {solution.isSymmetric(tree3)}")  # 应该输出True
    print(f"测试用例3 (迭代方法): {solution.isSymmetricIterative(tree3)}")  # 应该输出True