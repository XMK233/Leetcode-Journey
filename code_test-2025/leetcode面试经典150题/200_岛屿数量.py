from typing import List

'''给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1
示例 2：

输入：grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1' '''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """计算网格中岛屿的数量
        
        Args:
            grid: 二维网格，包含 '1'（陆地）和 '0'（水）
            
        Returns:
            int: 岛屿的数量
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        # DFS遍历函数，将访问过的陆地标记为水
        def dfs(i, j):
            # 边界条件：越界或不是陆地
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            # 标记为已访问（将陆地变为水）
            grid[i][j] = '0'
            
            # 向四个方向进行DFS
            dfs(i+1, j)  # 下
            dfs(i-1, j)  # 上
            dfs(i, j+1)  # 右
            dfs(i, j-1)  # 左
        
        # 遍历整个网格
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # 发现新的岛屿
                    count += 1
                    dfs(i, j)  # 用DFS遍历整个岛屿并标记
        
        return count


# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1：单个岛屿
    grid1 = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    print(f"测试用例1结果: {solution.numIslands([row.copy() for row in grid1])}")  # 预期输出: 1
    
    # 测试用例2：多个岛屿
    grid2 = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(f"测试用例2结果: {solution.numIslands([row.copy() for row in grid2])}")  # 预期输出: 3
    
    # 测试用例3：空网格
    grid3 = []
    print(f"测试用例3结果: {solution.numIslands(grid3)}")  # 预期输出: 0
    
    # 测试用例4：全是水
    grid4 = [
        ['0', '0', '0'],
        ['0', '0', '0']
    ]
    print(f"测试用例4结果: {solution.numIslands([row.copy() for row in grid4])}")  # 预期输出: 0
    
    # 测试用例5：全是陆地
    grid5 = [
        ['1', '1'],
        ['1', '1']
    ]
    print(f"测试用例5结果: {solution.numIslands([row.copy() for row in grid5])}")  # 预期输出: 1
        