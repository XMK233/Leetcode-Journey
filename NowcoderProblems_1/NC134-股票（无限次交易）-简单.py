# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/9e5e3c2603064829b0a0bbfca10594e9?tpId=117&&tqId=37846&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
'''
题目描述
假定你知道某只股票每一天价格的变动。
你最多可以同时持有一只股票。但你可以无限次的交易（买进和卖出均无手续费）。
请设计一个函数，计算你所能获得的最大收益。
示例1
输入
复制
[5,4,3,2,1]
返回值
复制
0
说明
由于每天股票都在跌，因此不进行任何交易最优。最大收益为0。

示例2
输入
复制
[1,2,3,4,5]
返回值
复制
4
说明
第一天买进，最后一天卖出最优。中间的当天买进当天卖出不影响最终结果。最大收益为4。

这道题看似困难, 实则简单. 至少最简单的方法的思路是很好理解的.
理论上, 只要没涨到最高就不卖. 一旦开始跌, 马上卖掉; 一旦跌到谷底马上买. 掌握上述理论, 就能获得最大化的利益. 是不是?
所以, 我们只要看当第i天的记录比前一天的高, 就在res里加上prices[i] - prices[i - 1]就行了.
自然就能求得最优解.
'''

class Solution:
    def maxProfit(self , prices ):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res

print(Solution().maxProfit([1, 5, 8, 4, 2, 3, 6, 4, 10, 7, 3, 2, 1, 6]))