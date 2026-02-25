'''中等
相关标签
premium lock icon
相关企业
提示
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100'''

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 设定四条边界：上、下、左、右。每一轮按“上行 -> 右列 -> 下行 -> 左列”顺序遍历
        # 然后向内收缩边界，直到所有元素都被访问
        if not matrix or not matrix[0]:
            return []
        res: List[int] = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            # 1. 从左到右遍历当前上边界所在行
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            # 上边界下移，下一轮不再包含这一行
            top += 1
            # 2. 从上到下遍历当前右边界所在列
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            # 右边界左移
            right -= 1
            # 3. 如果还有剩余行，沿着当前下边界从右到左遍历
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            # 4. 如果还有剩余列，沿着当前左边界从下到上遍历
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.spiralOrder(m1))  # [1,2,3,6,9,8,7,4,5]
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(sol.spiralOrder(m2))  # [1,2,3,4,8,12,11,10,9,5,6,7]
