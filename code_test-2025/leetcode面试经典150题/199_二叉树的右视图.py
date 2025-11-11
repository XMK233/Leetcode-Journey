'''给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

示例 1：

输入：root = [1,2,3,null,5,null,4]

输出：[1,3,4]

解释：



示例 2：

输入：root = [1,2,3,4,null,null,null,5]

输出：[1,3,4,5]

解释：



示例 3：

输入：root = [1,null,3]

输出：[1,3]
示例 4：

输入：root = []

输出：[]

 

提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100 
'''
from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        获取二叉树的右视图，即从右侧观察二叉树时能看到的节点值
        
        Args:
            root: 二叉树的根节点
            
        Returns:
            从顶部到底部顺序的右视图节点值列表
        """
        # 处理空树的情况
        if not root:
            return []
        
        result = []
        # 使用队列进行层序遍历（BFS）
        queue = deque([root])
        
        while queue:
            # 获取当前层的节点数量
            level_size = len(queue)
            
            # 遍历当前层的所有节点
            for i in range(level_size):
                node = queue.popleft()
                
                # 如果是当前层的最后一个节点，将其值添加到结果中
                if i == level_size - 1:
                    result.append(node.val)
                
                # 将左子节点加入队列
                if node.left:
                    queue.append(node.left)
                # 将右子节点加入队列
                if node.right:
                    queue.append(node.right)
        
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

# 测试用例1：[1,2,3,null,5,null,4]
# 预期输出：[1,3,4]
tree1 = build_tree([1,2,3,None,5,None,4])
result1 = solution.rightSideView(tree1)
print(f"测试用例1结果: {result1}")

# 测试用例2：[1,2,3,4,null,null,null,5]
# 预期输出：[1,3,4,5]
tree2 = build_tree([1,2,3,4,None,None,None,5])
result2 = solution.rightSideView(tree2)
print(f"测试用例2结果: {result2}")

# 测试用例3：[1,null,3]
# 预期输出：[1,3]
tree3 = build_tree([1,None,3])
result3 = solution.rightSideView(tree3)
print(f"测试用例3结果: {result3}")

# 测试用例4：[]
# 预期输出：[]
tree4 = build_tree([])
result4 = solution.rightSideView(tree4)
print(f"测试用例4结果: {result4}")