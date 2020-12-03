class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = '#' + s, '#' + p
        m, n = len(s), len(p)
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        for i in range(m):
            for j in range(1, n):
                if i == 0:
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j - 2]
                elif p[j] in [s[i], '.']:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    dp[i][j] = j > 1 and dp[i][j - 2] or p[j - 1] in [s[i], '.'] and dp[i - 1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]

print(Solution().isMatch("aab", "c*a*b"))

# 作者：loick
# 链接：https: // leetcode - cn.com / problems / zheng - ze - biao - da - shi - pi - pei - lcof / solution / dong - tai - gui - hua - er - wei - shu - zu - by - loick /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
## 利用动归来做，很好的思路，多学习学习