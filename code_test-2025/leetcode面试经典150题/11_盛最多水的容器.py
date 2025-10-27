"""
11. 盛最多水的容器

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

示例 1:
输入: height = [1,8,6,2,5,4,8,3,7]
输出: 49
解释: 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2:
输入: height = [1,1]
输出: 1

提示：
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        方法1: 双指针法
        使用双指针从数组的两端向中间移动
        
        算法思路：
        1. 初始化左右指针分别指向数组的首尾
        2. 计算当前容器的面积：面积 = 宽度 × 最小高度
        3. 移动指向较矮边界的指针（因为移动高边界不会增加面积）
        4. 重复直到左右指针相遇
        
        时间复杂度: O(n) - n为数组长度，每个元素最多被访问一次
        空间复杂度: O(1) - 只使用了常数个额外变量
        
        关键洞察：移动较矮的边界有可能找到更高的边界，从而增加面积
        """
        if not height or len(height) < 2:
            return 0
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 计算当前容器的面积
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # 更新最大面积
            max_area = max(max_area, current_area)
            
            # 移动指向较矮边界的指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
    def maxArea_v2(self, height: List[int]) -> int:
        """
        方法2: 优化的双指针法
        在方法1的基础上添加一些优化
        
        优化点：
        1. 跳过相同高度的边界（避免重复计算）
        2. 提前终止条件（如果当前最大面积已经不可能被超越）
        
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not height or len(height) < 2:
            return 0
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # 计算当前容器的面积
            width = right - left
            left_height = height[left]
            right_height = height[right]
            current_height = min(left_height, right_height)
            current_area = width * current_height
            
            # 更新最大面积
            max_area = max(max_area, current_area)
            
            # 移动指向较矮边界的指针，并跳过相同高度的边界
            if left_height < right_height:
                # 移动左指针，跳过相同高度的边界
                while left < right and height[left] <= left_height:
                    left += 1
            else:
                # 移动右指针，跳过相同高度的边界
                while left < right and height[right] <= right_height:
                    right -= 1
        
        return max_area
    
    def maxArea_v3(self, height: List[int]) -> int:
        """
        方法3: 暴力法（用于验证正确性）
        检查所有可能的边界组合
        
        算法思路：
        1. 对于每个左边界，尝试所有可能的右边界
        2. 计算每个组合的容器面积
        3. 返回最大面积
        
        时间复杂度: O(n²) - 需要检查所有n(n-1)/2种组合
        空间复杂度: O(1)
        
        注意：这种方法只适用于小规模数据，用于验证其他方法的正确性
        """
        if not height or len(height) < 2:
            return 0
        
        max_area = 0
        n = len(height)
        
        for left in range(n - 1):
            for right in range(left + 1, n):
                width = right - left
                current_height = min(height[left], height[right])
                current_area = width * current_height
                max_area = max(max_area, current_area)
        
        return max_area
    
    def maxArea_v4(self, height: List[int]) -> int:
        """
        方法4: 进一步优化（记录最大高度）
        在移动指针时记录已经见过的最大高度
        
        优化思路：
        1. 如果当前边界比之前见过的最矮边界还矮，可以直接跳过
        2. 因为这样的组合不可能产生更大的面积
        
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not height or len(height) < 2:
            return 0
        
        left = 0
        right = len(height) - 1
        max_area = 0
        max_left_height = 0
        max_right_height = 0
        
        while left < right:
            left_height = height[left]
            right_height = height[right]
            
            # 更新见过的最大高度
            max_left_height = max(max_left_height, left_height)
            max_right_height = max(max_right_height, right_height)
            
            # 计算当前面积
            width = right - left
            current_height = min(left_height, right_height)
            current_area = width * current_height
            max_area = max(max_area, current_area)
            
            # 移动指向较矮边界的指针
            if left_height < right_height:
                # 如果当前左边界比之前见过的最矮左边界还矮，跳过
                if left_height < max_left_height:
                    left += 1
                    continue
                left += 1
            else:
                # 如果当前右边界比之前见过的最矮右边界还矮，跳过
                if right_height < max_right_height:
                    right -= 1
                    continue
                right -= 1
        
        return max_area


def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),      # 基本测试
        ([1, 1], 1),                           # 两个相同高度的边界
        ([4, 3, 2, 1, 4], 16),                 # 两端高，中间低
        ([1, 2, 1], 2),                        # 中间高，两端低
        ([1, 2, 4, 3], 4),                     # 递增序列
        ([4, 3, 2, 1], 4),                     # 递减序列
        ([1, 8, 6, 2, 5, 4, 8, 3, 7, 8], 56),  # 更长的序列
        ([2, 3, 4, 5, 18, 17, 6], 17),         # 特殊情况
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25), # 递增长序列
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25), # 递减长序列
    ]
    
    print("测试盛最多水的容器问题：")
    print("=" * 50)
    
    for i, (height, expected) in enumerate(test_cases, 1):
        result1 = solution.maxArea(height)
        result2 = solution.maxArea_v2(height)
        result3 = solution.maxArea_v3(height)
        result4 = solution.maxArea_v4(height)
        
        print(f"测试用例 {i}: height = {height}")
        print(f"期望结果: {expected}")
        print(f"方法1结果: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"方法2结果: {result2} {'✓' if result2 == expected else '✗'}")
        print(f"方法3结果: {result3} {'✓' if result3 == expected else '✗'}")
        print(f"方法4结果: {result4} {'✓' if result4 == expected else '✗'}")
        print("-" * 30)


if __name__ == "__main__":
    test_solution()