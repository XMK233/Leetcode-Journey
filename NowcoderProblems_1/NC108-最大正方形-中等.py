# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/0058c4092cec44c2975e38223f10470e?tpId=117&&tqId=37832&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
'''
题目描述
给定一个由0和1组成的2维矩阵，返回该矩阵中最大的由1组成的正方形的面积
示例1
输入
复制
[[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]
返回值
复制
4

就是一个dp, dp数组表示以matrix[i][j]为右下角的最大正方形的边长.
递推公式是: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
后面的+1别忘了.
'''

#
# 最大正方形
# @param matrix char字符型二维数组
# @return int整型
#
class Solution:
    def solve(self , matrix ):
        # write code here
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxside = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1: ## 注意这里的判断，系统里面，是要判断是否为字符"1"而非数字1.
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxside = max(maxside, dp[i][j])
        return maxside * maxside

print(Solution().solve([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))