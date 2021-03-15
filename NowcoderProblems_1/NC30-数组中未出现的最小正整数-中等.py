# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/8cc4f31432724b1f88201f7b721aa391?tpId=117&&tqId=37800&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个无序数组arr，找到数组中未出现的最小正整数
例如arr = [-1, 2, 3, 4]。返回1
arr = [1, 2, 3, 4]。返回5
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)

示例1
输入
复制
[-1,2,3,4]
返回值
复制
1
备注:
1 \leq N \leq 10^61≤N≤10
6

|arr_i| \leq 10^9∣arr
i
​
 ∣≤10
9

O(n)的解法
看了一些题解都是hash或者排序、划分的解法，时间和空间复杂度都不满足要求。这里给一个时间复杂度O(n),空间复杂度O(1)的解法。
其实这个题目不太严谨，本质上是一个简单的数学问题。应该再加上一个条件：加上这个缺失的最小整数后，它是一个连续数组（不包括0）。
不知道是不是以为这个原因，很多朋友没有这么去想。

如果是连续数组，这个问题就简单多了：
我们先求出数组和，然后再计算出[min, max]连续区间的和。差值就是缺少的那个正数。
处理一下相等的情况就可以了。

'''
#
# return the min number
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def minNumberdisappered(self , arr ):
        # write code here
        aMin, aMax, sum1 = float("Inf"), float("-Inf"), 0 ## 这里一开始的时候没写对.
        for num in arr:
            if num <= 0: continue
            aMin = min(num, aMin)
            aMax = max(num, aMax)
            sum1 += num
        sum2 = 0
        for i in range(aMin, aMax + 1):
            sum2 += i
        if sum2 - sum1 == 0: ## 这个里面的条件判断, 一开始没有写对.
            ## 两种情况, 第一种是含有
            if aMin - 1 > 0: return aMin - 1
            else: return aMax + 1
        else:
            return sum2 - sum1

print(Solution().minNumberdisappered([-1, 2, 3, 4]))
