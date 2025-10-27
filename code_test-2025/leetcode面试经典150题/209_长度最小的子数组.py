"""
209. 长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1:
输入: target = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 满足该条件，所以返回 2。

示例 2:
输入: target = 4, nums = [1,4,4]
输出: 1

示例 3:
输入: target = 11, nums = [1,1,1,1,1]
输出: 0

提示：
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        方法1: 滑动窗口（双指针）
        使用滑动窗口来找到满足条件的最短子数组
        
        算法思路：
        1. 使用两个指针left和right表示滑动窗口的左右边界
        2. 使用变量current_sum来存储当前窗口内元素的和
        3. 当current_sum >= target时，尝试缩小窗口（移动left指针）
        4. 当current_sum < target时，扩大窗口（移动right指针）
        
        时间复杂度: O(n) - n为数组长度，每个元素最多被访问两次
        空间复杂度: O(1) - 只使用了常数个额外变量
        """
        if not nums:
            return 0
        
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            # 扩大窗口：将右边界元素加入当前和
            current_sum += nums[right]
            
            # 当当前和大于等于目标值时，尝试缩小窗口
            while current_sum >= target:
                # 更新最小长度
                min_length = min(min_length, right - left + 1)
                # 缩小窗口：将左边界元素从当前和中移除
                current_sum -= nums[left]
                left += 1
        
        # 如果没有找到符合条件的子数组，返回0
        return min_length if min_length != float('inf') else 0
    
    def minSubArrayLen_v2(self, target: int, nums: List[int]) -> int:
        """
        方法2: 前缀和 + 二分查找
        使用前缀和数组和二分查找来优化搜索过程
        
        算法思路：
        1. 计算前缀和数组prefix_sum，其中prefix_sum[i]表示前i个元素的和
        2. 对于每个位置i，使用二分查找找到最小的j，使得prefix_sum[j] - prefix_sum[i] >= target
        3. 这样可以在O(log n)时间内找到以i为起点的最短子数组
        
        时间复杂度: O(n log n) - 需要n次二分查找，每次二分查找O(log n)
        空间复杂度: O(n) - 需要额外的空间存储前缀和数组
        """
        if not nums:
            return 0
        
        n = len(nums)
        # 计算前缀和数组
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        min_length = float('inf')
        
        # 对于每个起点i，找到满足条件的最短子数组
        for i in range(n):
            # 需要找到最小的j，使得prefix_sum[j] - prefix_sum[i] >= target
            # 即prefix_sum[j] >= target + prefix_sum[i]
            target_sum = target + prefix_sum[i]
            
            # 二分查找
            left, right = i + 1, n
            while left <= right:
                mid = (left + right) // 2
                if prefix_sum[mid] >= target_sum:
                    min_length = min(min_length, mid - i)
                    right = mid - 1
                else:
                    left = mid + 1
        
        return min_length if min_length != float('inf') else 0
    
    def minSubArrayLen_v3(self, target: int, nums: List[int]) -> int:
        """
        方法3: 优化的滑动窗口（提前终止）
        在方法1的基础上添加一些优化
        
        优化点：
        1. 如果数组总和小于target，直接返回0
        2. 如果找到长度为1的子数组满足条件，可以直接返回1（最短可能长度）
        3. 使用更高效的变量更新方式
        
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not nums:
            return 0
        
        # 预检查：如果总和小于target，直接返回0
        if sum(nums) < target:
            return 0
        
        left = 0
        current_sum = 0
        min_length = len(nums)  # 初始化为最大可能长度
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum >= target:
                # 更新最小长度
                window_length = right - left + 1
                min_length = min(min_length, window_length)
                
                # 如果找到长度为1的子数组，直接返回（优化）
                if min_length == 1:
                    return 1
                
                current_sum -= nums[left]
                left += 1
        
        return min_length


def test_solution():
    """测试函数"""
    solution = Solution()
    
    # 测试用例
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3], 2),      # 基本测试：子数组[4,3]长度为2
        (4, [1, 4, 4], 1),               # 子数组[4]长度为1
        (11, [1, 1, 1, 1, 1], 0),        # 不存在满足条件的子数组
        (1, [1], 1),                      # 单个元素满足条件
        (15, [1, 2, 3, 4, 5], 5),        # 需要整个数组
        (6, [1, 2, 3, 4, 5], 2),         # 子数组[2,4]或[1,5]
        (100, [1, 2, 3], 0),              # 总和小于target
        (3, [1, 1, 1, 1, 1], 3),          # 需要3个元素
        (7, [2, 3, 1, 2, 4, 3, 7], 1),    # 存在单个元素满足条件
    ]
    
    print("测试长度最小的子数组问题：")
    print("=" * 50)
    
    for i, (target, nums, expected) in enumerate(test_cases, 1):
        result1 = solution.minSubArrayLen(target, nums)
        result2 = solution.minSubArrayLen_v2(target, nums)
        result3 = solution.minSubArrayLen_v3(target, nums)
        
        print(f"测试用例 {i}: target={target}, nums={nums}")
        print(f"期望结果: {expected}")
        print(f"方法1结果: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"方法2结果: {result2} {'✓' if result2 == expected else '✗'}")
        print(f"方法3结果: {result3} {'✓' if result3 == expected else '✗'}")
        print("-" * 30)


if __name__ == "__main__":
    test_solution()