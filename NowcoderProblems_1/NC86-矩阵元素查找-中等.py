# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/3afe6fabdb2c46ed98f06cfd9a20f2ce?tpId=117&&tqId=37788&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
已知int一个有序矩阵mat，同时给定矩阵的大小n和m以及需要查找的元素x，且矩阵的行和列都是从小到大有序的。设计查找算法返回所查找元素的二元数组，代表该元素的行号和列号(均从零开始)。保证元素互异。

示例1
输入
复制
[[1,2,3],[4,5,6]],2,3,6
返回值
复制
[1,2]

剑指offer04
'''
# -*- coding:utf-8 -*-

class Solution:
    def findElement(self, mat, n, m, x):
        matrix = mat
        target = x
        ## 这个i,j就说明了, 我们从左下角开始的.
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if matrix[i][j] == target:
                return [i, j]#True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return []# False
