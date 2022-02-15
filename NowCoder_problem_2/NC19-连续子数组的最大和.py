class Solution:
    def FindGreatestSumOfSubArray(self , array) -> int:
        # write code here
        dp = [i for i in array] ## This means that when the subarrays contain one element in each of them.
        res = array[0]
        for i in range(1, len(array)):
            dp[i] = max(
                dp[i-1] + array[i], ## multiple elements subarray
                array[i] ## single element subarray
            )
            res = max(res, dp[i])
        return res

print(
    Solution().FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5])
)

'''
描述
输入一个长度为n的整型数组array，数组中的一个或连续多个整数组成一个子数组，子数组最小长度为1。求所有子数组的和的最大值。
数据范围:
1 <= n <= 2\times10^51<=n<=2×10
5

-100 <= a[i] <= 100−100<=a[i]<=100

要求:时间复杂度为 O(n)O(n)，空间复杂度为 O(n)O(n)
进阶:时间复杂度为 O(n)O(n)，空间复杂度为 O(1)O(1)
示例1
输入：
[1,-2,3,10,-4,7,2,-5]
复制
返回值：
18
复制
说明：
经分析可知，输入数组的子数组[3,10,-4,7,2]可以求得最大和为18
示例2
输入：
[2]
复制
返回值：
2
复制
示例3
输入：
[-10]
复制
返回值：
-10
'''