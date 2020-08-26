class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums)+1)//2
        left, right = nums[:mid], nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]

## https://blog.csdn.net/danspace1/article/details/88527722
## 酱紫。
## 以后刷题，你就想着，哦，我先暴力求解一波。然后在暴力求解的基础上进行优化足矣。
## 或许这样反倒能够提供一些方便。
## 所以，这道题就非常简单。
## 将数组排序后，分前后两半，然后后半边倒序，然后再跟前一半组合就好了。