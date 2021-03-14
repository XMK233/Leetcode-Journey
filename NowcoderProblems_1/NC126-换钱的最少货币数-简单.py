# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/3911a20b3f8743058214ceaa099eeb45?tpId=117&&tqId=37795&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定数组arr，arr中所有的值都为正整数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个aim，代表要找的钱数，求组成aim的最少货币数。
如果无解，请返回-1.
【要求】
时间复杂度O(n \times aim)O(n×aim)，空间复杂度On。
示例1
输入
复制
[5,2,3],20
返回值
复制
4
示例2
输入
复制
[5,2,3],0
返回值
复制
0
示例3
输入
复制
[3,5],2
返回值
复制
-1
备注:
0 \leq n \leq 1\,0000≤n≤1000
0 \leq aim \leq 5\,0000≤aim≤5000

参考了别人的实现。以aim来建立dp数组。这是一个经典的dp问题。
'''
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
class Solution:
    def minMoney(self , arr , aim ):
        # write code here
        dp = [float('inf')] * (aim + 1)
        dp[0] = 0
        for i in range(aim + 1):
            for num in arr:
                if i >= num:
                    dp[i] = min(dp[i], dp[i - num] + 1)
        print(dp)
        return -1 if dp[aim] == float('inf') else dp[-1]

print(Solution().minMoney([5, 2, 3], 20))