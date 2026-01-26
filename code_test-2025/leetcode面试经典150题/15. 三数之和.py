'''中等
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 

提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        寻找数组中所有和为0的不重复三元组
        解题思路：排序 + 双指针
        时间复杂度：O(n²)，其中n是数组长度
        空间复杂度：O(1)或O(logn)（取决于排序算法）
        """
        # 1. 排序数组，便于后续双指针操作和去重
        nums.sort()
        result = []
        n = len(nums)
        
        # 2. 遍历数组，将当前元素作为三元组的第一个元素
        for i in range(n - 2):
            # 跳过重复的第一个元素，避免重复解
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3. 双指针初始化：左指针指向i+1，右指针指向数组末尾
            left, right = i + 1, n - 1
            target = -nums[i]  # 寻找两个数之和等于-target
            
            # 4. 双指针遍历，寻找符合条件的另外两个元素
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # 找到一个有效三元组，添加到结果中
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的左指针元素，避免重复解
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的右指针元素，避免重复解
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 双指针同时移动到下一个位置
                    left += 1
                    right -= 1
                elif current_sum < target:
                    # 当前和小于目标值，左指针右移增大和
                    left += 1
                else:
                    # 当前和大于目标值，右指针左移减小和
                    right -= 1
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: 有多个有效三元组的情况
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print("Example 1:")
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]]")
    print(f"Pass: {result1 == [[-1, -1, 2], [-1, 0, 1]]}\n")
    
    # Example 2: 没有有效三元组的情况
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    print("Example 2:")
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: []")
    print(f"Pass: {result2 == []}\n")
    
    # Example 3: 三个相同元素的情况
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    print("Example 3:")
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: [[0, 0, 0]]")
    print(f"Pass: {result3 == [[0, 0, 0]]}")
        