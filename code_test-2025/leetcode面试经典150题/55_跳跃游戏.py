#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
55. 跳跃游戏
中等

给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        判断是否能到达最后一个下标
        
        算法思路 - 贪心算法：
        1. 维护一个变量max_reach，表示当前能到达的最远位置
        2. 遍历数组，对于每个位置i：
           - 如果i超过了max_reach，说明无法到达当前位置，返回False
           - 更新max_reach为max(max_reach, i + nums[i])
        3. 如果遍历完成，说明可以到达最后一个位置，返回True
        
        时间复杂度: O(n) - 只需遍历一次数组
        空间复杂度: O(1) - 只使用了常数个额外变量
        """
        n = len(nums)
        if n <= 1:
            return True
        
        # max_reach表示当前能到达的最远位置
        max_reach = 0
        
        for i in range(n):
            # 如果当前位置超过了能到达的最远位置，返回False
            if i > max_reach:
                return False
            
            # 更新能到达的最远位置
            max_reach = max(max_reach, i + nums[i])
            
            # 如果能到达或超过最后一个位置，提前返回True
            if max_reach >= n - 1:
                return True
        
        return True
    
    def canJump_alternative(self, nums: List[int]) -> bool:
        """
        另一种思路 - 从后往前贪心：
        1. 维护一个变量last_pos，表示需要到达的最后位置（初始为最后一个位置）
        2. 从后往前遍历数组：
           - 如果当前位置i加上nums[i]能够到达last_pos，则更新last_pos为i
        3. 最后检查last_pos是否为0
        
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        n = len(nums)
        if n <= 1:
            return True
        
        # last_pos表示需要到达的最后位置
        last_pos = n - 1
        
        for i in range(n - 1, -1, -1):
            # 如果当前位置能够到达last_pos
            if i + nums[i] >= last_pos:
                last_pos = i
        
        return last_pos == 0

def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例1
    print("测试用例1:")
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.canJump(nums1)
    print(f"输入: {nums1}")
    print(f"输出: {result1}")
    print(f"预期: True")
    print()
    
    # 测试用例2
    print("测试用例2:")
    nums2 = [3, 2, 1, 0, 4]
    result2 = solution.canJump(nums2)
    print(f"输入: {nums2}")
    print(f"输出: {result2}")
    print(f"预期: False")
    print()
    
    # 测试用例3 - 单元素
    print("测试用例3:")
    nums3 = [0]
    result3 = solution.canJump(nums3)
    print(f"输入: {nums3}")
    print(f"输出: {result3}")
    print(f"预期: True")
    print()
    
    # 测试用例4 - 两个元素，可以到达
    print("测试用例4:")
    nums4 = [2, 0]
    result4 = solution.canJump(nums4)
    print(f"输入: {nums4}")
    print(f"输出: {result4}")
    print(f"预期: True")
    print()
    
    # 测试用例5 - 两个元素，不能到达
    print("测试用例5:")
    nums5 = [0, 2]
    result5 = solution.canJump(nums5)
    print(f"输入: {nums5}")
    print(f"输出: {result5}")
    print(f"预期: False")
    print()
    
    # 测试用例6 - 测试另一种算法
    print("测试用例6 - 使用另一种算法:")
    nums6 = [2, 3, 1, 1, 4]
    result6 = solution.canJump_alternative(nums6)
    print(f"输入: {nums6}")
    print(f"输出: {result6}")
    print(f"预期: True")
    print()
    
    # 测试用例7 - 测试另一种算法
    print("测试用例7 - 使用另一种算法:")
    nums7 = [3, 2, 1, 0, 4]
    result7 = solution.canJump_alternative(nums7)
    print(f"输入: {nums7}")
    print(f"输出: {result7}")
    print(f"预期: False")

if __name__ == "__main__":
    test_solution()