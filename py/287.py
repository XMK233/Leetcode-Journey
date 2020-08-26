class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid :
                right = mid - 1
            else:
                left = mid + 1
        return left
# https://blog.csdn.net/u014251967/article/details/52485452
## 我参考的解析里面，其实有一个隐含条件，没有说出来。
## 就是：
## 采用二分法的根本原理是什么？为什么二分法可以work？其实是以为，作者假定了
## 我们将原数组排序了，得到一个有序数组。但实际上并没有这一步操作。
## 因为排序了之后，1就本该在第一个位置上，2就本该在第二个位置上，类推。直到我们找到不当位的那个数字，也就是重复的数字了。
## 这个排序的数组其实就是一个假想的数组。