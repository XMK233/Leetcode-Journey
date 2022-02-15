# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/64b4262d4e6d4f6181cd45446a5821ec?tpId=117&&tqId=37717&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
假设你有一个数组，其中第\ i i 个元素是股票在第\ i i 天的价格。
你有一次买入和卖出的机会。（只有买入了股票以后才能卖出）。请你设计一个算法来计算可以获得的最大收益。
示例1
输入
复制
[1,4,2]
返回值
复制
3
示例2
输入
复制
[2,4,1]
返回值
复制
2

jianzhiOffer 63

#基本思路：假设当前a最小，当遇到b(b<a)时，我们可知：若后面出现的使得利益更大的价格C
#(max利润=C-a)，那么C-b一定大于C-a，即后面的最大收益的比较只需要通过b来计算
#(max利润=C-b），不再需要a了，因此，我们需要一个游标来记录和更新min值。

'''
class Solution:
    def maxProfit(self, prices) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p, max_p = float("Inf"), 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)

        return max_p