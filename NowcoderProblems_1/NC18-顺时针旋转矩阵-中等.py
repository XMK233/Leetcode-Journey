# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/2e95333fbdd4451395066957e24909cc?tpId=117&&tqId=37790&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。

给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵,保证N小于等于300。

示例1
输入
复制
[[1,2,3],[4,5,6],[7,8,9]],3
返回值
复制
[[7,4,1],[8,5,2],[9,6,3]]

技巧: 先求转置矩阵, 然后在每一行里求逆序.
# https://blog.csdn.net/qq_32424059/article/details/91904646
## 道理是酱紫的: 先求转置矩阵, 然后每一行再逆序.
## 其实直接求旋转应该也可以, 但是这样的技巧是可以大幅度降低编程的难度的, 也能让错误更少.
'''

# -*- coding:utf-8 -*-

class Solution:
    def rotateMatrix(self, mat, n):
        matrix = mat
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 先转置再左右对称翻转
        if not matrix or not matrix[0]:
            return matrix
#         n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            for i in range(n // 2):
                row[i], row[n - 1 - i] = row[n - 1 - i], row[i]

        return matrix

