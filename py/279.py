class Solution:
    def numSquares(self, n: 'int') -> 'int':
        dp = [n]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[-1]

## https://blog.csdn.net/danspace1/article/details/87820924
## 道理上来讲，跟用几块钱硬币去凑某个面值的题是一样的。
##