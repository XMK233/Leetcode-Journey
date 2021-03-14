# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/554aa508dd5d4fefbf0f86e5fe953abd?tpId=117&&tqId=37797&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个数组arr，返回子数组的最大累加和
例如，arr = [1, -2, 3, 5, -2, 6, -1]，所有子数组中，[3, 5, -2, 6]可以累加出最大的和12，所以返回12.
题目保证没有全为负数的数据
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)

示例1
输入
复制
[1, -2, 3, 5, -2, 6, -1]
返回值
复制
12
备注:
1 \leq N \leq 10^51≤N≤10
5

|arr_i| \leq 100∣arr
i
​
 ∣≤100

用一个dp算法, 参考剑指offer42题
'''

#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxsumofSubarray(self , arr ):
# https://blog.csdn.net/fuxuemingzhu/article/details/71101802
## 参考这个人的解析里面的状态转移公式.
        nums = arr
        if not nums: return 0
        N = len(nums)
        cur, prev = 0, 0
        res = float("-inf")
        for i in range(N):
            cur = nums[i] + (prev if prev > 0 else 0)
            prev = cur
            res = max(res, cur)
        return res

## 答案的思路是：构建dp数组，dp[i]的意义是，以这个nums[i]结尾的数组里面最大的和。
## 当然了，这个解并没有构建一个dp数组，可能是因为作者将其优化了吧。