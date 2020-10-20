class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else: grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]

## https://www.pythonheidong.com/blog/article/546114/
## 道理非常简单, 其实就是这里的dp递推原理是: 判断从起点(0, 0)到(i,j)这个点的最大收益是多少.
## 重复一遍, 是从起点开始到某点的最大收益.
### 如果是第一行位置, 那么最大收益只能是从左边来的; 如果是第一列的位置, 那么最大收益只能是从上面来的.
### 如果是其他位置, 那么最大收益就非常简单了, 就是来源于(i-1, j)(i, j - 1)两个位置更大的那个点.