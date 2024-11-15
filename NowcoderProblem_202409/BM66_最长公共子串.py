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
# 1 0 1 0 0 0 0 0 0 0 0
# 2 0 0 0 0 1 0 0 0 0 0
# 3 0 0 0 0 0 2 0 0 0 0
# 4 0 0 0 0 0 0 3 0 0 0
# 5 0 0 0 0 0 0 0 4 0 0
# E 0 0 0 0 0 0 0 0 0 0
# F 0 0 0 0 0 0 0 0 0 0


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# longest common substring
# @param str1 string字符串 the string
# @param str2 string字符串 the string
# @return string字符串
#
class Solution:
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        dp = [[0 for _ in range(len(str1))] for __ in range(len(str2))]
        ## 这里的dp记录的是，最后一个位置为str2[i]和str1[j]时，最长连续字符串。
        ## 这个最长连续字符串必须是以str2[i]或者str1[j]结尾的，如果这俩位置的自负不同，那么整个最长子串长度就为0了。
        ## 这个跟最长子序列的求法不同，要注意。
        ## 最幽默的是，按照官方给的方法，居然会超时。。。我也是醉了。
        max_pos = (-1, -1)
        max_length = -1
        for i in range(len(str2)):
            for j in range(len(str1)):
                if i == 0 or j == 0:
                    if str2[i] == str1[j]: ## 如果两个字符串的当前位置的值一样，则。。。
                        dp[i][j] = dp[max(0, i - 1)][max(0, j-1)] + 1 ## 把上面的或者是左边的dp值加1.
                else:
                    if str2[i] == str1[j]:  ## 如果两个字符串的当前位置的值一样，则。。。
                        dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        max_pos = (i, j)
        return str1[max_pos[1]-max_length+1:max_pos[1]+1]

print(Solution().LCS("1AB2345CD","12345EF"))

