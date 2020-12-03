class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        ##
        if len(s) == 1:
            return 1
        ##
        dp = [1] * (len(s) + 1)
        dp[1] = 1
        for i in range(1, len(s)):
            sec = int(s[i - 1 : i + 1])
            if s[i - 1] != "0" and sec >= 0 and sec <= 25:
                dp[i + 1] = dp[i + 1 - 2] + dp[i + 1 - 1]
            else:
                dp[i + 1] = dp[i + 1 - 1]
        return dp[-1]

s = Solution()
print(s.translateNum(506))

## 没有看解析, 直接自己写的.
## 思路就是, 建立一个比原字符串长1的dp数组, 初始值都为1.
## 然后呢, 遍历原字符串. 如果遍历到当前的i能和前面的那一个字符组合成0~25之间的数字, 那就有两种组合情况, 一种是这个i为单独的字符串, 一种是i和前面一个组合
### 成一个数字的情况. 两种情况能凑成的解法数量加起来就可以了.
### 注意, 这里有一个坑. 就是如果i前面那一个字符是0, 是不能看作"i和前面一个字符可以组合成一个数字"的哦.
## 然后, 如果i不能和前面一个字符组成合法数字, 那就只能把i当成一个单独的字符来翻译了. 