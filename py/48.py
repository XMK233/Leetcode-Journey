class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 先转置再左右对称翻转
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = row[n - 1 - i], row[i]

        return matrix

# https://blog.csdn.net/qq_32424059/article/details/91904646
## 道理是酱紫的: 先求转置矩阵, 然后每一行再逆序.
## 其实直接求旋转应该也可以, 但是这样的技巧是可以大幅度降低编程的难度的, 也能让错误更少.