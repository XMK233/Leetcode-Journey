'''
[面试题 17.09. 第 k 个数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/get-kth-magic-number-lcci)

有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9

'''

'''
本质上就是丑数啦. 参考剑指offer的49题. 
'''

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        UglyList = [1]
        index3 = 0
        index5 = 0
        index7 = 0
        for i in range(k - 1):
            newUgly = min(UglyList[index3] * 3, UglyList[index5] * 5, UglyList[index7] * 7)
            UglyList.append(newUgly)
            if newUgly % 3 == 0:
                index3 += 1
            if newUgly % 5 == 0:
                index5 += 1
            if newUgly % 7 == 0:
                index7 += 1
        return UglyList[-1]


