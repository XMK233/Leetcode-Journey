class Solution:
    def twoSum(self, n: int):
        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1

        for i in range(2,n+1):
            for j in range(i,i*6+1):
                for k in range(1,7):
                    if j >= k+1:
                        dp[i][j] +=dp[i-1][j-k]
        res = []
        for i in range(n,n*6+1):
            res.append(dp[n][i]*1.0/6**n)
        return res


## https://blog.csdn.net/qq_24243877/article/details/104560944
## 乃动态规划之解法，甚佳。宜当时习之。
