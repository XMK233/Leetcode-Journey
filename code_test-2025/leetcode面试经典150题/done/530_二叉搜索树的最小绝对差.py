'''给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。

 

示例 1：


输入：root = [4,2,6,1,3]
输出：1
示例 2：


输入：root = [1,0,48,null,null,12,49]
输出：1
 

提示：

树中节点的数目范围是 [2, 104]
0 <= Node.val <= 105
 

注意：本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同'''
from typing import Optional
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉搜索树中任意两个不同节点值之间的最小绝对差值
        
        Args:
            root: 二叉搜索树的根节点
            
        Returns:
            树中任意两不同节点值之间的最小绝对差值
        """
        # 用于存储前一个节点值和最小差值的容器
        result = {'prev': None, 'min_diff': sys.maxsize}
        
        # 递归中序遍历函数
        def inorder(node):
            if not node:
                return
            
            # 先遍历左子树
            inorder(node.left)
            
            # 处理当前节点
            ## xmk：这里真的是一个我没注意到的一个点。
            ## 首先，因为是二叉搜索树，所以最小差值肯定是相邻两个节点之间的差值。
            ## 因为是递归的嘛，所以我们只用专注研究某节点和它左边邻居节点之间的差值便可。
            ## 然后，因为是中序遍历，所以左边节点值一定是当前节点的前一个节点。
            ## 中序遍历的特性就是，遍历的顺序就是从左到右的，非常顺畅。
            ## 所以你不要问为什么，只要本轮递归中把当前点记录下来（prev = node.val），下次再中序到某一节点的时候，
            ## prev节点就恰恰好是左子树最右边的节点，也就是中序遍历成数组之后本节点左边邻居节点。
            ## 这个属性真的太神奇了，瞬间让我神清气爽。
            if result['prev'] is not None:
                # 计算当前节点与前一个节点的差值
                current_diff = node.val - result['prev']
                # 更新最小差值
                if current_diff < result['min_diff']:
                    result['min_diff'] = current_diff
            # 更新前一个节点的值
            result['prev'] = node.val
            
            # 再遍历右子树
            inorder(node.right)
        
        # 执行递归中序遍历
        inorder(root)
        
        return result['min_diff']


# 辅助函数：根据列表构建二叉树
# 列表表示形式：[根, 左, 右, 左左, 左右, 右左, 右右, ...]
# None表示该位置没有节点

def build_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    while queue and i < len(nodes):
        node = queue.pop(0)
        
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

# 测试用例1：[4,2,6,1,3]
# 预期输出：1
tree1 = build_tree([4,2,6,1,3])
result1 = solution.getMinimumDifference(tree1)
print(f"测试用例1结果: {result1}")

# 测试用例2：[1,0,48,None,None,12,49]
# 预期输出：1
tree2 = build_tree([1,0,48,None,None,12,49])
result2 = solution.getMinimumDifference(tree2)
print(f"测试用例2结果: {result2}")

# 测试用例3：[90,69,100,49,89,None,None,None,80]
# 预期输出：1
tree3 = build_tree([90,69,100,49,89,None,None,None,80])
result3 = solution.getMinimumDifference(tree3)
print(f"测试用例3结果: {result3}")

# 测试用例4：[5,1,49,None,None,12,48]
# 预期输出：1
tree4 = build_tree([5,1,49,None,None,12,48])
result4 = solution.getMinimumDifference(tree4)
print(f"测试用例4结果: {result4}")