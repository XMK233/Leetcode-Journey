## https://blog.csdn.net/fuxuemingzhu/article/details/81126995
## DFS的道理我能懂.
## 但是这个思路真是妙啊.
## 从一个1开始dfs, 把它邻接的点全部涂成0, 然后看总共需要进行几次的dfs才能把整个地图涂成0.
## 要涂几次, 有几个岛屿.
### 思路绝了啊~~~

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)