class Solution:
    def addDigits(self, num: int) -> int:
        ## 这道题需要用一个叫digit root的技巧来解. 详见https://en.wikipedia.org/wiki/Digital_root
        ## 参考解法 https://blog.csdn.net/NoMasp/article/details/50392541
        ## 按照它的公式里面, 编程如下:
        if num == 0:
            return 0
        else:
            if num % 9 == 0:
                return 9
            else:
                return num % 9

s = Solution()
print(s.addDigits(38))