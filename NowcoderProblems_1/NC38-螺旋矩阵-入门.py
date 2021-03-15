# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/7edf70f2d29c4b599693dc3aaeea1d31?tpId=117&&tqId=37738&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

螺旋打印矩阵.

剑指offer29

'''
#
#
# @param matrix int整型二维数组
# @return int整型一维数组
#
class Solution:
    def spiralOrder(self , matrix ):
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res
