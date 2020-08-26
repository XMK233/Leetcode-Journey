## https://blog.csdn.net/asd136912/article/details/79572128
## 思路是, 以1开头的子集, 以2 开头的子集, 以3开头的子集, 类推
## 然后用dfs对这些子集是可以进行组合的.

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, path + [nums[i]], res)
        res = []
        nums.sort()
        dfs(nums, 0, [], res)
        return res