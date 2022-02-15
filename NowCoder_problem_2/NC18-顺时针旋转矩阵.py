'''
描述
有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。

给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵。

数据范围：0 < n < 3000<n<300，矩阵中的值满足 0 \le val \le 10000≤val≤1000

要求：空间复杂度 O(N^2)O(N
2
 )，时间复杂度 O(N^2)O(N
2
 )
进阶：空间复杂度 O(1)O(1)，时间复杂度 O(N^2)O(N
2
 )
示例1
输入：
[[1,2,3],[4,5,6],[7,8,9]],3
复制
返回值：
[[7,4,1],[8,5,2],[9,6,3]]
'''

class Solution:
    ## 自己做的，纯粹就是找规律。
    def rotateMatrix(self , mat, n):
        # write code here
        def new_cord(old_row, old_col, start, end):
            new_row = old_col
            if old_row == start:
                new_col = end
            elif old_row == end:
                new_col = start
            else: ## 这个地方一开始没找对。
                new_col = n - 1 - old_row
            return new_row, new_col

        start, end = 0, n-1

        while end > start:
            tmps = []
            ## for the first row:
            for c in range(start, end):
                new_row, new_col = new_cord(start, c, start, end)
                tmps.append(mat[new_row][new_col])
                mat[new_row][new_col] = mat[start][c]
            ## for the last col:
            for r in range(start, end):
                new_row, new_col = new_cord(r, end, start, end)
                tmps.append(mat[new_row][new_col])
                mat[new_row][new_col] = tmps.pop(0)
            ## for the last row:
            for c in range(end, start, -1):
                new_row, new_col = new_cord(end, c, start, end)
                tmps.append(mat[new_row][new_col])
                mat[new_row][new_col] = tmps.pop(0)
            ## for the first col:
            for r in range(end, start, -1):
                new_row, new_col = new_cord(r, start, start, end)
                mat[new_row][new_col] = tmps.pop(0)
            end -= 1
            start += 1

        return mat

print(
    Solution().rotateMatrix(
        [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]], 5
    )
)
