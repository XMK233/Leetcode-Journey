## https://blog.csdn.net/NXHYD/article/details/71588665
## 没有完全理解参考思路.
## 但是基本上能够确定的是呢, 尽量把0往前面放, 2往后面放. 然后用两个flag来标定0区间和2区间.
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums== []:
            return
        p0 = 0
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 +=1
                i += 1
            else:
                i += 1