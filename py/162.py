class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                left = mid2
            else:
                right = mid1
        return left

## https://blog.csdn.net/fuxuemingzhu/article/details/79633332
## 记得用二分查找哦.
## 二分查找, 找左边递增, 右边递减的那种情况.