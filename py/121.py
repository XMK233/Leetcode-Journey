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

# https://blog.csdn.net/mabozi08/article/details/88995635
# max(
#     今天不卖（也就是之前几天的最大收益），
#     今天卖出然后和之前的最小值之间的差价（随时更新最小值看样子是会得到负数的，但是由于还要取最大值，所以就算出现负数也绝对不会被记录下来）
# )