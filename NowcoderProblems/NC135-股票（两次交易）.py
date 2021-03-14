## 思路很简单，非常好理解，直接看代码就好了。
## 直接的思路就是：分五种情况进行dp，见下述的 dp0到dp4

'''
题目描述
假定你知道某只股票每一天价格的变动。
你最多可以同时持有一只股票。但你最多只能进行两次交易（一次买进和一次卖出记为一次交易。买进和卖出均无手续费）。
请设计一个函数，计算你所能获得的最大收益。
示例1
输入
复制
[8,9,3,5,1,3]
返回值
复制
4
说明
第三天买进，第四天卖出，第五天买进，第六天卖出。总收益为4。
备注:
总天数不大于200000。保证股票每一天的价格在[1,100]范围内。

用dp算法，非常简单。见代码吧。

'''

class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0

        dp0 = 0  # 一直不买，那就没有收益也没有损失
        dp1 = - prices[0]  # 到最后也只买入了一笔，那初始化的时候，就是亏了第一股的钱
        dp2 = float("-inf")  # 到最后买入一笔，卖出一笔，后面的dp都是收益无限小。
        dp3 = float("-inf")  # 到最后买入两笔，卖出一笔
        dp4 = float("-inf")  # 到最后买入两笔，卖出两笔

        for i in range(1, len(prices)):
            dp1 = max(dp1, dp0 - prices[i]) ## 跟一直不买比
            dp2 = max(dp2, dp1 + prices[i]) ## 后面的dp，都是跟上一个dp相比。
            dp3 = max(dp3, dp2 - prices[i])
            dp4 = max(dp4, dp3 + prices[i])
        return max(dp0, dp2, dp4)

# 作者：edelweisskoko
# 链接：https: // leetcode - cn.com / problems / best - time - to - buy - and -sell - stock - iii / solution / yi - kan - jiu - dong - de - jian - dan - ti - jie - by - ed - 0o3l /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。