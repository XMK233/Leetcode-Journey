#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self , nums: list[int], target: int) -> int:
        # write code here
        if len(nums) == 0:
            return -1

        def search_helper(nums, target, idx_start, idx_end):
            if idx_start > idx_end:
                return -1
            idx_mid = (idx_start + idx_end) // 2
            if nums[idx_mid] == target:
                return idx_mid
            if nums[idx_mid] < target:
                return search_helper(nums, target, idx_mid+1, idx_end)
            else:
                return search_helper(nums, target, idx_start, idx_mid-1)

        return search_helper(nums, target, 0, len(nums)-1)

s = Solution()
print(s.search([-1,0,3,4,6,10,13,14],2))