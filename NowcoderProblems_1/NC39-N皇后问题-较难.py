# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c76408782512486d91eea181107293b6?tpId=117&&tqId=37811&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
NN皇后问题是指在N*NN∗N的棋盘上要摆NN个皇后，
要求：任何两个皇后不同行，不同列也不再同一条斜线上，
求给一个整数NN，返回NN皇后的摆法数。
示例1
输入
复制
1
返回值
复制
1
示例2
输入
复制
8
返回值
复制
92
备注:
1 \leq n \leq 141≤n≤14


参考自最优解书。
'''

class Solution:
    def Nqueen(self , n ):
        # write code here
        records = [0] * n ## records[i]表示第i行放置的列数。
        def isPuttable(i, j):
            for k in range(i): ## 遍历之前放置的皇后
                ## k是之前的行， records[k]是之前的列
                if records[k] == j or abs(k - i) == abs(records[k] - j): ## 判断不同列，不同斜线。为什么不判断不同行？卧槽这不是自然的嘛，还用另行判断吗？
                    return False
            return True
        def dfs(i): ## 判断第i行该怎么放
            if i == n: ## 这里是什么意思呢？因为如果i==n的话，实际上是放不了的，因为行号最大为n-1. 所以如果i==n了，就说明这个遍历结束了，返回一个基本状态，就是1。
                return 1
            ##
            res = 0
            for j in range(n):
                if isPuttable(i, j):
                    records[i] = j ## 记录，第i行的棋子摆在了j这个列上
                    res += dfs(i + 1)
            return res
        return dfs(0)

print(
    Solution().Nqueen(8)
)