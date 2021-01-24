'''
[剑指 Offer 14- II. 剪绳子 II - 力扣（LeetCode）](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof)

给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

 

提示：


	2 <= n <= 1000


注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
'''

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j]*(i-j), j*(i-j)) #
        return dp[-1] % 1000000007

# 作者：mao-mao-mao-m
# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/dong-tai-gui-hua-wu-shu-xue-fei-zhao-gui-lu-by-mao/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

print(Solution().cuttingRope(10))

## 微创新了一下前一题。实际上唯一一处变化就是最后答案模上一个数字。
## 居然也能AC。但是结果发现，时间和空间复杂度都很大。确实是这样的。

## 思路还算明晰。比很多答案的数学证明，说什么尽量分成三段、每段差不多相等就能得到最大乘积，之类的要简单。
## dp是一个数组，i指的是当这条绳子全长为i的时候。所以dp【i】指的是当绳子只有长度i的时候，能得到的最大乘积。
## j的范围仅为1到i之间。表示：如果j到i长度是完整的绳子。
## 所以，
### dp【i】就保留当前的最大乘积；
### dp[j]*(i-j)指的是，j之前的绳子经过裁剪，乘上j->i这段完整绳子的长度得到的乘积；
### j*(i-j)表示j之前的长度不裁剪，也就是长度为i的绳子只剪一刀就是在j处，能得到的最大乘积。


##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()