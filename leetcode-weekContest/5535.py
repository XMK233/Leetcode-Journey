## 最大嵌套深度.
## 怎么破?

class Solution:
    def maxDepth(self, s: str) -> int:
        curLayer = 0
        maxLayer = 0
        for c in s:
            if c == "(":
                curLayer += 1
                maxLayer = max(curLayer, maxLayer)
            elif c == ")":
                curLayer -= 1

        return maxLayer

s = Solution()
print(s.maxDepth(
"1"
))
## tnd, 这就AC了...