class Solution:
    def countDigitOne(self, n: int) -> int:
        countr = 0
        i = 1
        while i <= n:
            divider = i * 10
            countr += (n//divider) * i + min(max(n%divider - i + 1, 0), i)
            i *= 10
        return countr
## https://leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode/
## 没看懂。