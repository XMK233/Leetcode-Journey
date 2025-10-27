#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
80. 删除有序数组中的重复项 II
中等

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3 。不需要考虑数组中超出新长度后面的元素。

提示：
1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums 已按升序排列
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        删除有序数组中的重复项 II - 每个元素最多出现两次
        
        算法思路 - 双指针：
        1. 使用慢指针slow跟踪新数组的末尾位置
        2. 使用快指针fast遍历原数组
        3. 维护一个计数器count记录当前元素的重复次数
        4. 当count <= 2时，将元素复制到slow位置
        5. 当元素改变时，重置计数器
        
        时间复杂度: O(n) - 只需遍历一次数组
        空间复杂度: O(1) - 只使用了常数个额外变量
        """
        n = len(nums)
        if n <= 2:
            return n
        
        # slow指针指向新数组的末尾位置
        slow = 2
        
        # 从第3个元素开始遍历
        for fast in range(2, n):
            # 如果当前元素与前一个元素不同，或者与前一个元素相同但与slow-2位置不同
            # 这意味着当前元素可以保留（要么是新元素，要么是第二次出现）
            if nums[fast] != nums[slow - 1] or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
    
    def removeDuplicates_v2(self, nums: List[int]) -> int:
        """
        另一种思路 - 使用计数器：
        1. 使用慢指针slow跟踪新数组的末尾位置
        2. 使用计数器count记录当前元素的重复次数
        3. 当count <= 2时，将元素保留
        
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        n = len(nums)
        if n <= 2:
            return n
        
        slow = 1
        count = 1  # 当前元素的重复次数
        
        for fast in range(1, n):
            if nums[fast] == nums[fast - 1]:
                # 相同元素，增加计数
                count += 1
            else:
                # 不同元素，重置计数
                count = 1
            
            # 如果计数小于等于2，保留该元素
            if count <= 2:
                slow += 1
                nums[slow - 1] = nums[fast]
        
        return slow

def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例1
    print("测试用例1:")
    nums1 = [1, 1, 1, 2, 2, 3]
    nums1_copy = nums1.copy()
    result1 = solution.removeDuplicates(nums1_copy)
    print(f"输入: {nums1}")
    print(f"输出长度: {result1}")
    print(f"修改后的数组: {nums1_copy[:result1]}")
    print(f"预期长度: 5")
    print(f"预期数组: [1, 1, 2, 2, 3]")
    print()
    
    # 测试用例2
    print("测试用例2:")
    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    nums2_copy = nums2.copy()
    result2 = solution.removeDuplicates(nums2_copy)
    print(f"输入: {nums2}")
    print(f"输出长度: {result2}")
    print(f"修改后的数组: {nums2_copy[:result2]}")
    print(f"预期长度: 7")
    print(f"预期数组: [0, 0, 1, 1, 2, 3, 3]")
    print()
    
    # 测试用例3 - 空数组
    print("测试用例3:")
    nums3 = []
    nums3_copy = nums3.copy()
    result3 = solution.removeDuplicates(nums3_copy)
    print(f"输入: {nums3}")
    print(f"输出长度: {result3}")
    print(f"修改后的数组: {nums3_copy[:result3]}")
    print(f"预期长度: 0")
    print(f"预期数组: []")
    print()
    
    # 测试用例4 - 单个元素
    print("测试用例4:")
    nums4 = [1]
    nums4_copy = nums4.copy()
    result4 = solution.removeDuplicates(nums4_copy)
    print(f"输入: {nums4}")
    print(f"输出长度: {result4}")
    print(f"修改后的数组: {nums4_copy[:result4]}")
    print(f"预期长度: 1")
    print(f"预期数组: [1]")
    print()
    
    # 测试用例5 - 所有元素相同
    print("测试用例5:")
    nums5 = [1, 1, 1, 1, 1]
    nums5_copy = nums5.copy()
    result5 = solution.removeDuplicates(nums5_copy)
    print(f"输入: {nums5}")
    print(f"输出长度: {result5}")
    print(f"修改后的数组: {nums5_copy[:result5]}")
    print(f"预期长度: 2")
    print(f"预期数组: [1, 1]")
    print()
    
    # 测试用例6 - 使用第二种算法
    print("测试用例6 - 使用第二种算法:")
    nums6 = [1, 1, 1, 2, 2, 3]
    nums6_copy = nums6.copy()
    result6 = solution.removeDuplicates_v2(nums6_copy)
    print(f"输入: {nums6}")
    print(f"输出长度: {result6}")
    print(f"修改后的数组: {nums6_copy[:result6]}")
    print(f"预期长度: 5")
    print(f"预期数组: [1, 1, 2, 2, 3]")

if __name__ == "__main__":
    test_solution()