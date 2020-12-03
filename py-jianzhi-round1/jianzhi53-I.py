class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return 0
        return right - left

    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))

### https://blog.csdn.net/fuxuemingzhu/article/details/83273084
## 这道题就是判断目标值的higher和lower边界何在.
## 你发现这两个方法有什么区别了没有. 一个是小于号, 另一个是小等于.
## 这两个方法, 建议直接背住就好了. 以后可能用得上. 这是个技巧.