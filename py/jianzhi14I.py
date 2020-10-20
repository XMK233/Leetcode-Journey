class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j]*(i-j), j*(i-j)) #
        return dp[-1]

# 作者：mao-mao-mao-m
# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/dong-tai-gui-hua-wu-shu-xue-fei-zhao-gui-lu-by-mao/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

print(Solution().cuttingRope(10))

## 思路还算明晰。比很多答案的数学证明，说什么尽量分成三段、每段差不多相等就能得到最大乘积，之类的要简单。
## dp是一个数组，i指的是当这条绳子全长为i的时候。所以dp【i】指的是当绳子只有长度i的时候，能得到的最大乘积。
## j的范围仅为1到i之间。表示：如果j到i长度是完整的绳子。
## 所以，
### dp【i】就保留当前的最大乘积；
### dp[j]*(i-j)指的是，j之前的绳子经过裁剪，乘上j->i这段完整绳子的长度得到的乘积；
### j*(i-j)表示j之前的长度不裁剪，也就是长度为i的绳子只剪一刀就是在j处，能得到的最大乘积。