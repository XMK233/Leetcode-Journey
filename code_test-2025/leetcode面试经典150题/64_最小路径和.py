"""
64. 最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

约束条件：
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 100
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        方法1: 动态规划（二维DP数组）
        使用二维DP数组记录到达每个位置的最小路径和
        
        算法思路：
        1. dp[i][j] 表示从起点到位置 (i,j) 的最小路径和
        2. 状态转移：dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        3. 边界条件：第一行和第一列只能从一个方向到达
        
        时间复杂度: O(m*n) - 需要遍历整个网格
        空间复杂度: O(m*n) - 需要二维DP数组
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        # 初始化起点
        dp[0][0] = grid[0][0]
        
        # 初始化第一列（只能从上往下走）
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # 初始化第一行（只能从左往右走）
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # 填充DP数组
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]
    
    def minPathSum_optimized(self, grid: List[List[int]]) -> int:
        """
        方法2: 动态规划（一维DP数组优化）
        使用一维数组优化空间复杂度
        
        算法思路：
        由于dp[i][j]只依赖于dp[i-1][j]和dp[i][j-1]，可以用一维数组优化
        
        时间复杂度: O(m*n) - 需要遍历整个网格
        空间复杂度: O(n) - 只需要一维DP数组
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        
        # 初始化第一行
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        
        # 逐行更新
        for i in range(1, m):
            # 更新第一列
            dp[0] += grid[i][0]
            
            # 更新其他列
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        
        return dp[n-1]
    
    def minPathSum_inplace(self, grid: List[List[int]]) -> int:
        """
        方法3: 原地修改（最优空间复杂度）
        直接在原数组上进行修改，不需要额外的DP数组
        
        算法思路：
        直接在原grid数组上更新，利用同样的状态转移方程
        
        时间复杂度: O(m*n) - 需要遍历整个网格
        空间复杂度: O(1) - 原地修改，不需要额外空间
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # 初始化第一列（只能从上往下走）
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # 初始化第一行（只能从左往右走）
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # 填充剩余部分
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]
    
    def minPathSum_recursive(self, grid: List[List[int]]) -> int:
        """
        方法4: 递归 + 记忆化
        使用递归和记忆化搜索
        
        算法思路：
        从终点开始，递归计算到起点的最小路径和
        
        时间复杂度: O(m*n) - 每个位置只计算一次
        空间复杂度: O(m*n) - 需要记忆化数组和递归栈
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        memo = {}
        
        def dfs(i, j):
            # 到达起点
            if i == 0 and j == 0:
                return grid[0][0]
            
            # 检查记忆化
            if (i, j) in memo:
                return memo[(i, j)]
            
            # 边界处理
            if i < 0 or j < 0:
                return float('inf')
            
            # 递归计算
            from_top = dfs(i-1, j) if i > 0 else float('inf')
            from_left = dfs(i, j-1) if j > 0 else float('inf')
            
            result = grid[i][j] + min(from_top, from_left)
            memo[(i, j)] = result
            return result
        
        return dfs(m-1, n-1)


def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例1：基本测试
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    expected1 = 7
    print(f"测试用例1: {grid1}")
    print(f"期望结果: {expected1}")
    print(f"方法1结果: {solution.minPathSum(grid1)}")
    print(f"方法2结果: {solution.minPathSum_optimized(grid1)}")
    print(f"方法3结果: {solution.minPathSum_inplace([[1,3,1],[1,5,1],[4,2,1]])}")  # 重新传入，因为方法3会修改原数组
    print(f"方法4结果: {solution.minPathSum_recursive(grid1)}")
    print()
    
    # 测试用例2：基本测试
    grid2 = [[1,2,3],[4,5,6]]
    expected2 = 12
    print(f"测试用例2: {grid2}")
    print(f"期望结果: {expected2}")
    print(f"方法1结果: {solution.minPathSum(grid2)}")
    print(f"方法2结果: {solution.minPathSum_optimized(grid2)}")
    print(f"方法3结果: {solution.minPathSum_inplace([[1,2,3],[4,5,6]])}")
    print(f"方法4结果: {solution.minPathSum_recursive(grid2)}")
    print()
    
    # 测试用例3：单行
    grid3 = [[1,2,3,4,5]]
    expected3 = 15
    print(f"测试用例3: {grid3}")
    print(f"期望结果: {expected3}")
    print(f"方法1结果: {solution.minPathSum(grid3)}")
    print(f"方法2结果: {solution.minPathSum_optimized(grid3)}")
    print(f"方法3结果: {solution.minPathSum_inplace([[1,2,3,4,5]])}")
    print(f"方法4结果: {solution.minPathSum_recursive(grid3)}")
    print()
    
    # 测试用例4：单列
    grid4 = [[1],[2],[3],[4],[5]]
    expected4 = 15
    print(f"测试用例4: {grid4}")
    print(f"期望结果: {expected4}")
    print(f"方法1结果: {solution.minPathSum(grid4)}")
    print(f"方法2结果: {solution.minPathSum_optimized(grid4)}")
    print(f"方法3结果: {solution.minPathSum_inplace([[1],[2],[3],[4],[5]])}")
    print(f"方法4结果: {solution.minPathSum_recursive(grid4)}")
    print()
    
    # 测试用例5：1x1网格
    grid5 = [[5]]
    expected5 = 5
    print(f"测试用例5: {grid5}")
    print(f"期望结果: {expected5}")
    print(f"方法1结果: {solution.minPathSum(grid5)}")
    print(f"方法2结果: {solution.minPathSum_optimized(grid5)}")
    print(f"方法3结果: {solution.minPathSum_inplace([[5]])}")
    print(f"方法4结果: {solution.minPathSum_recursive(grid5)}")
    print()
    
    # 测试用例6：包含0的网格
    grid6 = [[0,0,0],[0,1,0],[0,0,0]]
    expected6 = 1
    print(f"测试用例6: {grid6}")
    print(f"期望结果: {expected6}")
    print(f"方法1结果: {solution.minPathSum(grid6)}")
    print(f"方法2结果: {solution.minPathSum_optimized(grid6)}")
    print(f"方法3结果: {solution.minPathSum_inplace([[0,0,0],[0,1,0],[0,0,0]])}")
    print(f"方法4结果: {solution.minPathSum_recursive(grid6)}")
    print()


if __name__ == "__main__":
    test_solution()