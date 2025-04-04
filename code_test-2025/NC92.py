## NC92 最长公共子序列(二)

class Solution:
    def LCS(self, s1, s2):
        # write code here
        m, n = len(s1), len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        ans = ''
        i, j = m, n
        while i >= 1 and j >= 1:
            if s1[i - 1] == s2[j - 1]:
                ans += s1[i - 1]
                i -= 1
                j -= 1
            elif dp[i][j - 1] >= dp[i - 1][j]: ## 这里是大于还是大等于都行欸。
                j -= 1
            else:
                i -= 1
        if not ans: return -1
        return ans[::-1]

print(
    Solution().LCS(
        # "algorithms", "alchemist"
"1A2C3D4B56","B1D23A456A"
    )
)