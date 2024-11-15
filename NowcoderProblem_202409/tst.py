# ("1AB2345CD",
#
#
#
#  "12345EF")
#
#
#
#   0 1 A B 2 3 4 5 C D
# 0 0 0 0 0 0 0 0 0 0 0
# 1 0 1 1 1 1 1 1 1 1 1
# 2 0 1 1 1 2 2 2 2 2 2
# 3 0 1 1 1 2 3 3 3 3 3
# 4 0 1 1 1 2 3 4 4 4 4
# 5 0 1 1 1 2 3 4 5 5 5
# E 0 1 1 1 2 3 4 5 5 5
# F 0 1 1 1 2 3 4 5 5 5

class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        dp = [[0 for _ in range(len(str1) + 1)] for __ in range(len(str2) + 1)]
        ## 这里的dp记录的是，最后一个位置为str2[i]和str1[j]时，最长连续字符串。
        ## 这个最长连续字符串必须是以str2[i]或者str1[j]结尾的，如果这俩位置的自负不同，那么整个最长子串长度就为0了。
        ## 这个跟最长子序列的求法不同，要注意。
        ## 最幽默的是，按照官方给的方法，居然会超时。。。我也是醉了。
        max_pos = (-1, -1)
        max_length = -1
        for i in range(1, len(str2) + 1):
            for j in range(1, len(str1) + 1):
                if str2[i-1] == str1[j-1]:  ## 如果两个字符串的当前位置的值一样，则。。。
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(
                        dp[i][j-1], dp[i-1][j]
                    )
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    max_pos = (i, j)
        print(dp, max_pos)

        ## 寻找最长的序列：
        ### 核心思想就是，看当前位置dp[i][j]对应的str1和str2字符是不是相同，如果是的话就记录这个字符然后往左上走；
        ### 否则就看往左和往上走的话，哪个的dp更大，就往更大的方向走就好了。
        i_, j_ = max_pos
        lth = max_length
        rst = ""
        while lth > 0:
            if str2[i_ - 1] == str1[j_ - 1]:
                rst += str2[i_ - 1]
                i_-=1
                j_-=1
                lth -= 1
            else:
                if dp[i_][j_ - 1] > dp[i_ - 1][j_]:
                    j_ -= 1
                else:
                    i_ -= 1

        return rst[::-1]

print(Solution().LCS("1AB2345CD","12x345EF"))


