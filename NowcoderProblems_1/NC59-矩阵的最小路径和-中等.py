# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/7d21b6be4c6b429bb92d219341c4f8bb?tpId=117&&tqId=37823&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
示例1
输入
复制
[[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
返回值
复制
12
备注:
1 \leq n,m \leq 20001≤n,m≤2000
1 \leq arr_{i,j} \leq 1001≤arr
i,j
​
 ≤100

 很简单的思路,dp就好了. 都不用建立二维的dp数组.

'''


#
#
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self, matrix):
        # write code here
        if not matrix:
            return 0

        n = len(matrix[0])
        dp = [0] * n
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == 0 and j == 0:
                    dp[j] = matrix[i][j]
                elif i == 0:
                    dp[j] = dp[j - 1] + matrix[i][j]
                elif j == 0:
                    dp[j] = dp[j] + matrix[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + matrix[i][j]
        return dp[-1]