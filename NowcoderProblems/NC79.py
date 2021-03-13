# -*- coding:utf-8 -*-
## 丑数，不必说。
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        ## 首先进行简单判断：
        if index == 0:
            return 0
        ## 一般情况
        uglyNums = [1]
        index2, index3, index5 = 0, 0, 0
        for i in range(index - 1):
            nextUglyNum = min(uglyNums[index2] * 2, uglyNums[index3] * 3, uglyNums[index5] * 5)
            uglyNums.append(nextUglyNum)
            if nextUglyNum % 2 == 0:
                index2 += 1
            if nextUglyNum % 3 == 0:
                index3 += 1
            if nextUglyNum % 5 == 0:
                index5 += 1
        return uglyNums[-1]

print(Solution().GetUglyNumber_Solution(7))