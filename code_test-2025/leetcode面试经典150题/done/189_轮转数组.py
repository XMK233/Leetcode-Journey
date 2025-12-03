#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
轮转数组
中等

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

示例 2:
输入: nums = [-1,-100,3,99], k = 2
输出: [3,99,-1,-100]
解释:
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        方法1: 使用额外的数组
        创建一个新数组，将元素放到正确的位置上
        
        时间复杂度: O(n)
        空间复杂度: O(n) - 需要额外的数组
        """
        n = len(nums)
        if n <= 1 or k == 0:
            return
        
        k = k % n  # 处理k大于n的情况
        result = [0] * n
        
        for i in range(n):
            result[(i + k) % n] = nums[i]
        
        # 将结果复制回原数组
        for i in range(n):
            nums[i] = result[i]
    
    def rotate_v2(self, nums: List[int], k: int) -> None:
        """
        方法2: 环状替换
        将元素逐个移动到它们最终的位置上
        
        时间复杂度: O(n)
        空间复杂度: O(1) - 原地算法
        """
        n = len(nums)
        if n <= 1 or k == 0:
            return
        
        k = k % n  # 处理k大于n的情况
        count = 0  # 记录已经放置的元素数量
        start = 0  # 起始位置
        
        while count < n:
            current = start
            prev = nums[start]
            
            while True:
                # 计算下一个位置
                next_pos = (current + k) % n
                # 保存下一个位置的值
                temp = nums[next_pos]
                # 将当前值放到下一个位置
                nums[next_pos] = prev
                # 更新prev为保存的值
                prev = temp
                # 移动到下一个位置
                current = next_pos
                # 增加计数
                count += 1
                
                # 如果回到了起始位置，跳出循环
                if current == start:
                    break
            
            # 移动到下一个起始位置
            start += 1
    
    def rotate_v3(self, nums: List[int], k: int) -> None:
        """
        方法3: 三次反转
        1. 反转整个数组
        2. 反转前k个元素
        3. 反转剩下的元素
        
        时间复杂度: O(n)
        空间复杂度: O(1) - 原地算法
        """
        n = len(nums)
        if n <= 1 or k == 0:
            return
        
        k = k % n  # 处理k大于n的情况
        
        # 1. 反转整个数组
        self.reverse(nums, 0, n - 1)
        # 2. 反转前k个元素
        self.reverse(nums, 0, k - 1)
        # 3. 反转剩下的元素
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """辅助函数：反转数组的指定部分"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate_v4(self, nums: List[int], k: int) -> None:
        """
        方法4: Python切片（最简单的方法）
        
        时间复杂度: O(n)
        空间复杂度: O(n) - 切片会创建新数组
        """
        n = len(nums)
        if n <= 1 or k == 0:
            return
        
        k = k % n  # 处理k大于n的情况
        nums[:] = nums[-k:] + nums[:-k]

def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例1
    print("测试用例1:")
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    nums1_copy = nums1.copy()
    solution.rotate(nums1_copy, k1)
    print(f"输入: nums = {nums1}, k = {k1}")
    print(f"输出: {nums1_copy}")
    print(f"预期: [5, 6, 7, 1, 2, 3, 4]")
    print()
    
    # 测试用例2
    print("测试用例2:")
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    nums2_copy = nums2.copy()
    solution.rotate(nums2_copy, k2)
    print(f"输入: nums = {nums2}, k = {k2}")
    print(f"输出: {nums2_copy}")
    print(f"预期: [3, 99, -1, -100]")
    print()
    
    # 测试用例3 - k大于数组长度
    print("测试用例3:")
    nums3 = [1, 2, 3]
    k3 = 4
    nums3_copy = nums3.copy()
    solution.rotate(nums3_copy, k3)
    print(f"输入: nums = {nums3}, k = {k3}")
    print(f"输出: {nums3_copy}")
    print(f"预期: [3, 1, 2]")
    print()
    
    # 测试用例4 - 空数组
    print("测试用例4:")
    nums4 = []
    k4 = 1
    nums4_copy = nums4.copy()
    solution.rotate(nums4_copy, k4)
    print(f"输入: nums = {nums4}, k = {k4}")
    print(f"输出: {nums4_copy}")
    print(f"预期: []")
    print()
    
    # 测试用例5 - 单个元素
    print("测试用例5:")
    nums5 = [1]
    k5 = 3
    nums5_copy = nums5.copy()
    solution.rotate(nums5_copy, k5)
    print(f"输入: nums = {nums5}, k = {k5}")
    print(f"输出: {nums5_copy}")
    print(f"预期: [1]")
    print()
    
    # 测试用例6 - 使用方法2（环状替换）
    print("测试用例6 - 使用方法2（环状替换）:")
    nums6 = [1, 2, 3, 4, 5, 6]
    k6 = 2
    nums6_copy = nums6.copy()
    solution.rotate_v2(nums6_copy, k6)
    print(f"输入: nums = {nums6}, k = {k6}")
    print(f"输出: {nums6_copy}")
    print(f"预期: [5, 6, 1, 2, 3, 4]")
    print()
    
    # 测试用例7 - 使用方法3（三次反转）
    print("测试用例7 - 使用方法3（三次反转）:")
    nums7 = [1, 2, 3, 4, 5, 6, 7]
    k7 = 3
    nums7_copy = nums7.copy()
    solution.rotate_v3(nums7_copy, k7)
    print(f"输入: nums = {nums7}, k = {k7}")
    print(f"输出: {nums7_copy}")
    print(f"预期: [5, 6, 7, 1, 2, 3, 4]")
    print()
    
    # 测试用例8 - 使用方法4（Python切片）
    print("测试用例8 - 使用方法4（Python切片）:")
    nums8 = [1, 2, 3, 4, 5]
    k8 = 2
    nums8_copy = nums8.copy()
    solution.rotate_v4(nums8_copy, k8)
    print(f"输入: nums = {nums8}, k = {k8}")
    print(f"输出: {nums8_copy}")
    print(f"预期: [4, 5, 1, 2, 3]")

if __name__ == "__main__":
    test_solution()