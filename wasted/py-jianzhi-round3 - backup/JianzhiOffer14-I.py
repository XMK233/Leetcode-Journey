'''
[剑指 Offer 14- I. 剪绳子 - 力扣（LeetCode）](https://leetcode-cn.com/problems/jian-sheng-zi-lcof)

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：


	2 <= n <= 58


注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
'''
'''
## 思路还算明晰。比很多答案的数学证明，说什么尽量分成三段、每段差不多相等就能得到最大乘积，之类的要简单。
## dp是一个数组，i指的是当这条绳子全长为i的时候。所以dp【i】指的是当绳子只有长度i的时候，能得到的最大乘积。
## j的范围仅为1到i之间。表示：如果j到i长度是完整的绳子。
## 所以，
### dp【i】就保留当前的最大乘积；
### dp[j]*(i-j)指的是，j之前的绳子经过裁剪，乘上j->i这段完整绳子的长度得到的乘积；
### j*(i-j)表示j之前的长度不裁剪，也就是长度为i的绳子只剪一刀就是在j处，能得到的最大乘积。

# 作者：mao-mao-mao-m
# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/dong-tai-gui-hua-wu-shu-xue-fei-zhao-gui-lu-by-mao/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        ## 为什么要多一格?
        ### 因为哈, i表示绳子的长度, 自然是要从2开始的, 多一格的话会把这个过程表现得比较自然.
        ### 否则, i就得从1开始, 比较别扭. 但是只要你不嫌麻烦, 逻辑理得通, 从1开始也可以.
        dp = [1]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j]*(i-j), j*(i-j)) #
        return dp[-1]

print(Solution().cuttingRope(10))