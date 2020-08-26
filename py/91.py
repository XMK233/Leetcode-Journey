## https://blog.csdn.net/fuxuemingzhu/article/details/82120874
## 参考了上面方法, 自己尝试实现. 
## dp的部分原理, 算是搞明白了. 但是具体的实现还是有问题. 
## 于是就直接抄了. 

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ##
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            # if i == 0:
            #     dp[i+1] = 1
            # else:
            part1 = 0
            if s[i] != "0":
                part1 = dp[i - 1 + 1]
            ##
            part2 = 0
            if s[i - 1:i + 1] >= "10" and s[i - 1:i + 1] <= '26':
                part2 = dp[i - 2 + 1]

            # ##
            # part2 = 0
            # if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
            #     part2 = dp[i-2 + 1]
            # ##
            # part1 = dp[i-1 + 1]
            # ##
            dp[i + 1] = part1 + part2

        return dp[-1]