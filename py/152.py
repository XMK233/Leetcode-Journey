class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = [0] * N
        g = [0] * N
        f[0] = g[0] = res = nums[0]
        for i in range(1, N):
            f[i] = max(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            g[i] = min(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            res = max(res, f[i])
        return res

# https://blog.csdn.net/fuxuemingzhu/article/details/83211451
# 精髓在于, 记录两个值, 也就是, 遍历到当前点的时候, 最大/小的乘积是多少.
## 因为原数组当中的数字是有正负的, 正负号之施, 乘积大小之势异也. 原来最大的, 乘上负数, 也变成最小的了; 原来最小的反之.
## 所以要同时记录最大和最小的值. 然后每次都要对比三个数的大小:
## 上一个最大值乘上当前值的积; 上一个最小值乘上当前值的积; 当前值.
## 三者中最大的值, 将作为最新的记录.

## 所以精髓还是在于记录当前的最大最小值吧.