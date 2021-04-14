# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/f33f5adc55f444baa0e0ca87ad8a6aac?tpId=117&&tqId=37799&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。
示例1
输入
复制
"1AB2345CD","12345EF"
返回值
复制
"2345"
备注:
1 \leq |str_1|, |str_2| \leq 5\,0001≤∣str
1
​
 ∣,∣str
2
​
 ∣≤5000

思路比较直白, 就是dp动归. 没什么花活, 看看代码即可懂得.
注意这里的dp存储的是, 以s1[i]和s2[j]为结尾的字符串的最长公共子串.
所以, 如果s1[i]!=s2[j], 那么dp[i][j]是要为0的, 而不是像其他的dp题那样用max, min什么的进行递推.
'''

class Solution:
    def LCS(self, str1, str2):
        # write code here
        s1 = "#" + str1
        s2 = "#" + str2
        m, n = len(s1), len(s2)
        maxs, ind = 0, 0
        dp = [[0] * (n) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if maxs < dp[i][j]:
                        maxs = dp[i][j]
                        ind = i
        if maxs == 0:
            return ""
        return s1[ind - maxs + 1: ind + 1]