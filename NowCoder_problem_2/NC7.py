class Solution:
    def maxProfit(self , prices) -> int:
        '''
        大概就是记录最小的值是多少，然后每一天都试图卖出，看看能不能挣更多钱。
        :param prices:
        :return:
        '''
        # write code here
        if not prices:
            return 0
        min_val = prices[0]
        max_profit = 0
        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)
        return max_profit

print(
    Solution().maxProfit([8,9,2,5,4,7,1])
)