'''给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
 

提示：

2 <= nums.length <= 105
-30 <= nums[i] <= 30
输入 保证 数组 answer[i] 在  32 位 整数范围内
 

进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        计算除自身以外数组的乘积
        
        :param nums: 输入的整数数组
        :return: 输出的乘积数组
        """
        # 处理边界情况
        if not nums or len(nums) <= 1:
            return []
        
        # 初始化输出数组，所有元素先设为1
        answer = [1] * len(nums)
        
        # 从左到右遍历，计算前缀乘积
        prefix_product = 1
        for i in range(len(nums)):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        
        # 从右到左遍历，计算后缀乘积并与前缀乘积相乘
        suffix_product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        
        return answer