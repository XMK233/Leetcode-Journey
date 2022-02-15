class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        n = len(A)
        def helper(A, start1, start2, length):
            i, j = start1, start2
            while i >= 0 and j <= length-1 and A[i] == A[j]:
                i -= 1
                j += 1
            return j - i - 1

        res = 1 ## 这个取决于，如果没有回文串，那应该返回多少。
        for i in range(n-1):
            res = max(
                res,
                helper(A, i, i, n),
                helper(A, i, i+1, n)
            )
        return res

s = "1234567"
print(
    Solution().getLongestPalindrome(
        s
    )
)

