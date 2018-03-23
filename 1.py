class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        dic = {}
        nums_length = len(nums)
        for n in range(nums_length):
            if nums[n] in dic:
                result.append(dic[nums[n]])
                result.append(n)
                break
                pass
            else:
                dic[target - nums[n]] = n
        return result