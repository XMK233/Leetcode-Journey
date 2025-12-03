# 226. 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        翻转一棵二叉树
        
        思路解析（递归方法）：
        1. 如果当前节点为空，直接返回None
        2. 交换当前节点的左右子节点
        3. 递归地翻转当前节点的左子树
        4. 递归地翻转当前节点的右子树
        5. 返回当前节点
        
        参数:
            root: Optional[TreeNode] - 二叉树的根节点
        
        返回:
            Optional[TreeNode] - 翻转后的二叉树根节点
        """
        # 基本情况：如果节点为空，直接返回None
        if not root:
            return None
        
        # 交换当前节点的左右子节点
        root.left, root.right = root.right, root.left
        
        # 递归翻转左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 返回翻转后的节点
        return root
    
    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        使用迭代方法翻转二叉树
        
        思路解析（迭代方法）：
        1. 使用队列来存储待处理的节点
        2. 初始时将根节点加入队列（如果不为空）
        3. 当队列不为空时：
           - 取出队列中的一个节点
           - 交换该节点的左右子节点
           - 如果左子节点不为空，将其加入队列
           - 如果右子节点不为空，将其加入队列
        4. 返回根节点
        
        参数:
            root: Optional[TreeNode] - 二叉树的根节点
        
        返回:
            Optional[TreeNode] - 翻转后的二叉树根节点
        """
        # 如果根节点为空，直接返回None
        if not root:
            return None
        
        # 使用队列来存储待处理的节点
        queue = deque([root])
        
        while queue:
            # 取出队列中的一个节点
            node = queue.popleft()
            
            # 交换该节点的左右子节点
            node.left, node.right = node.right, node.left
            
            # 如果左子节点不为空，将其加入队列
            if node.left:
                queue.append(node.left)
            
            # 如果右子节点不为空，将其加入队列
            if node.right:
                queue.append(node.right)
        
        # 返回翻转后的根节点
        return root

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
    
    # 辅助函数：将二叉树转换为列表（层序遍历）
    def treeToList(root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # 移除末尾的None值
        while result and result[-1] is None:
            result.pop()
        
        return result
    
    # 测试用例1: 完整二叉树
    # 树结构: [4,2,7,1,3,6,9]
    #       4
    #      / \
    #     2   7
    #    / \ / \
    #   1  3 6  9
    tree1 = buildTree([4, 2, 7, 1, 3, 6, 9])
    print(f"原始树1: {treeToList(tree1)}")
    inverted1 = solution.invertTree(tree1)
    print(f"翻转后1 (递归方法): {treeToList(inverted1)}")  # 应该输出[4,7,2,9,6,3,1]
    
    # 测试用例2: 单节点树
    # 树结构: [1]
    tree2 = buildTree([1])
    print(f"原始树2: {treeToList(tree2)}")
    inverted2 = solution.invertTreeIterative(tree2)
    print(f"翻转后2 (迭代方法): {treeToList(inverted2)}")  # 应该输出[1]
    
    # 测试用例3: 空树
    tree3 = buildTree([])
    print(f"原始树3: {treeToList(tree3)}")
    inverted3 = solution.invertTree(tree3)
    print(f"翻转后3 (递归方法): {treeToList(inverted3)}")  # 应该输出[]
    
    # 测试用例4: 不完全二叉树
    # 树结构: [2,1,3]
    #     2
    #    / \
    #   1   3
    tree4 = buildTree([2, 1, 3])
    print(f"原始树4: {treeToList(tree4)}")
    inverted4 = solution.invertTreeIterative(tree4)
    print(f"翻转后4 (迭代方法): {treeToList(inverted4)}")  # 应该输出[2,3,1]