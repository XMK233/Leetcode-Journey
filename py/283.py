class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                slow += 1
            fast += 1

    def moveZeroes(self, nums):
        length = len(nums)
        slow = 0
        fast = 0
        while True:
            ## slow找第一个是0的数
            while slow < length:
                if nums[slow] == 0:
                    break
                slow += 1
            ## fast找第一个不是0的数
            fast = slow + 1
            while fast < length:
                if nums[fast] != 0:
                    break
                fast += 1
            ## fast接触到最后了, 可以退出了可以直接退出了.
            if fast >= length:
                return
            ## 否则, 就移动
            nums[slow] = nums[fast]
            nums[fast] = 0

## https://blog.csdn.net/coder_orz/java/article/details/51384498

s = Solution()
l = [1, 2, 3]
s.moveZeroes(l)
print(l)