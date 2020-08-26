class Solution:
    def canWinNim(self, n: int) -> bool:
        ## 小于三个, 那我一把赢.
        if n <= 3:
            return True
        ## 大于三个, 那就试着先拿走1, 2, 3个, 然后判断.
        return not(self.canWinNim(n-1)) or not(self.canWinNim(n-2)) or not(self.canWinNim(n-3))

s = Solution()
print(s.canWinNim(4))