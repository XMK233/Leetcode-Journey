# https://blog.csdn.net/fuxuemingzhu/article/details/71101802
## 参考这个人的解析里面的状态转移公式.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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