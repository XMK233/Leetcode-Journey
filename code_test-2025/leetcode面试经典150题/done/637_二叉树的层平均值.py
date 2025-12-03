"""给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。

 

示例 1：



输入：root = [3,9,20,null,null,15,7]
输出：[3.00000,14.50000,11.00000]
解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。
示例 2:



输入：root = [3,9,20,15,7]
输出：[3.00000,14.50000,11.00000]
 

提示：

树中节点数量在 [1, 104] 范围内
-231 <= Node.val <= 231 - 1"""
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        计算二叉树每一层节点的平均值
        
        Args:
            root: 二叉树的根节点
            
        Returns:
            包含每一层平均值的列表
        """
        # 由于题目保证输入是非空二叉树，这里可以不需要处理root为None的情况
        result = []
        # 使用队列进行层序遍历（BFS）
        queue = deque([root])
        
        while queue:
            # 获取当前层的节点数量
            level_size = len(queue)
            level_sum = 0
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                node = queue.popleft()
                # 累加当前层的节点值
                level_sum += node.val
                
                # 将左子节点加入队列
                if node.left:
                    queue.append(node.left)
                # 将右子节点加入队列
                if node.right:
                    queue.append(node.right)
            
            # 计算当前层的平均值并添加到结果中
            level_average = level_sum / level_size
            result.append(level_average)
        
        return result


# 辅助函数：根据列表构建二叉树
# 列表表示形式：[根, 左, 右, 左左, 左右, 右左, 右右, ...]
# None表示该位置没有节点

def build_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        node = queue.popleft()
        
        # 处理左子节点
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # 处理右子节点
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root


# 测试用例
solution = Solution()

# 测试用例1：[3,9,20,null,null,15,7]
# 预期输出：[3.0, 14.5, 11.0]
tree1 = build_tree([3,9,20,None,None,15,7])
result1 = solution.averageOfLevels(tree1)
print(f"测试用例1结果: {result1}")

# 测试用例2：[3,9,20,15,7]
# 预期输出：[3.0, 14.5, 11.0]
tree2 = build_tree([3,9,20,15,7])
result2 = solution.averageOfLevels(tree2)
print(f"测试用例2结果: {result2}")

# 测试用例3：[1]
# 预期输出：[1.0]
tree3 = build_tree([1])
result3 = solution.averageOfLevels(tree3)
print(f"测试用例3结果: {result3}")

# 测试用例4：[2147483647,2147483647,2147483647]
# 预期输出：[2147483647.0, 2147483647.0]
tree4 = build_tree([2147483647,2147483647,2147483647])
result4 = solution.averageOfLevels(tree4)
print(f"测试用例4结果: {result4}")