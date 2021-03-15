# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/166eaff8439d4cd898e3ba933fbc6358?tpId=117&&tqId=37736&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
一个机器人在m×n大小的地图的左上角（起点）。
机器人每次向下或向右移动。机器人要到达地图的右下角（终点）。
可以有多少种不同的路径从起点走到终点？

备注：m和n小于等于100,并保证计算结果在int范围内

示例1
输入
复制
2,1
返回值
复制
1
示例2
输入
复制
2,2
返回值
复制
2

应该来说是最简单的DP了.
'''
#
#
# @param m int整型
# @param n int整型
# @return int整型
#
class Solution:
    def uniquePaths(self , m , n ):
        # dp = [[0]*n for _ in range(m)]
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    # dp[i][j] = 1
                    dp[j] = 1
                else:
                    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    dp[j] = dp[j - 1] + dp[j]
        return dp[-1]#dp[-1][-1]
        # write code here